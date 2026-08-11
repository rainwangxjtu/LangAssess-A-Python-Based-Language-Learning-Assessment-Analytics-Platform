"""
progress.py

Longitudinal student progress analysis for Units 1-11.

Focus:
    - Listening
    - Reading
    - Four error types:
        1. Grammar
        2. Vocabulary Retention
        3. Discourse Analysis
        4. Socio-cultural Background Knowledge

Expected files:
    unit1.csv
    unit2.csv
    ...
    unit11.csv

Each CSV should have the same column structure.

The first row may contain a grouping header such as:

    Unit 1 | Error type | Error type | ...

The actual column names should be on the second row.

Speaking is intentionally excluded from the analysis.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONSTANTS
# ============================================================

ERROR_TYPES = [
    "Grammar",
    "Vocabulary Retention",
    "Discourse Analysis",
    "Socio-cultural Background Knowledge",
]

SKILLS = [
    "Listening",
    "Reading",
]

UNITS = list(range(1, 12))


# ============================================================
# COLUMN DEFINITIONS
# ============================================================

def get_expected_columns():
    """
    Return all required columns for the Listening/Reading
    longitudinal analysis.
    """

    columns = ["Student"]

    for skill in SKILLS:

        columns.append(
            f"{skill} Total"
        )

        for error_type in ERROR_TYPES:

            columns.append(
                f"{skill} {error_type}"
            )

    return columns


# ============================================================
# DATA LOADING
# ============================================================

def _read_csv_with_header_detection(file_path):
    """
    Read a CSV while supporting both:

    1. A normal CSV with one header row.
    2. A Unit CSV with an extra grouping row above
       the actual column names.

    Returns:
        pandas.DataFrame
    """

    # First try the first row as the header.
    first = pd.read_csv(
        file_path,
        header=0
    )

    first_columns = [
        str(column).strip()
        for column in first.columns
    ]

    if "Student" in first_columns:

        return first

    # If Student was not found, assume the second row
    # contains the real column names.
    second = pd.read_csv(
        file_path,
        header=1
    )

    return second


def load_unit_data(file_path, unit=None):
    """
    Load one Unit CSV file.

    Args:
        file_path:
            Path to the CSV file.

        unit:
            Unit number, such as 1 or 2.

    Returns:
        Clean DataFrame containing a Unit column.
    """

    df = _read_csv_with_header_detection(
        file_path
    )

    # Clean column names.
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Remove completely empty rows.
    df = df.dropna(
        how="all"
    )

    # Remove completely empty columns.
    df = df.dropna(
        axis=1,
        how="all"
    )

    # --------------------------------------------------------
    # Student
    # --------------------------------------------------------

    if "Student" not in df.columns:

        raise ValueError(
            f"{file_path} does not contain "
            "'Student' as a column."
        )

    df["Student"] = (
        df["Student"]
        .astype(str)
        .str.strip()
    )

    # Remove invalid student rows.
    df = df[
        (df["Student"] != "")
        & (df["Student"].str.lower() != "nan")
    ].copy()

    # --------------------------------------------------------
    # Numeric columns
    # --------------------------------------------------------

    for column in get_expected_columns():

        if column == "Student":
            continue

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Unit
    # --------------------------------------------------------

    if unit is None:

        filename = Path(
            file_path
        ).stem.lower()

        digits = "".join(
            character
            for character in filename
            if character.isdigit()
        )

        if digits:

            unit = int(digits)

        else:

            unit = np.nan

    df["Unit"] = unit

    return df


# ============================================================
# VALIDATION
# ============================================================

def validate_unit_data(df):
    """
    Return a list of missing required columns.
    """

    expected = set(
        get_expected_columns()
    )

    actual = set(
        df.columns
    )

    return sorted(
        expected - actual
    )


def check_unit_data(df):
    """
    Raise an error if required columns are missing.
    """

    missing = validate_unit_data(
        df
    )

    if missing:

        raise ValueError(
            "The following required columns are missing:\n"
            + "\n".join(
                f"- {column}"
                for column in missing
            )
        )


# ============================================================
# LOAD UNITS 1-11
# ============================================================

def load_all_units(data_folder):
    """
    Automatically load Unit 1 through Unit 11.

    Expected filenames:

        unit1.csv
        unit2.csv
        ...
        unit11.csv

    The following naming styles are also supported:

        Unit1.csv
        unit_1.csv
        Unit_1.csv

    Missing unit files are skipped.

    Returns:
        Combined DataFrame.
    """

    data_folder = Path(
        data_folder
    )

    frames = []

    for unit in UNITS:

        possible_files = [

            data_folder / f"unit{unit}.csv",

            data_folder / f"Unit{unit}.csv",

            data_folder / f"unit_{unit}.csv",

            data_folder / f"Unit_{unit}.csv",
        ]

        file_path = None

        for candidate in possible_files:

            if candidate.exists():

                file_path = candidate

                break

        # Missing units are allowed.
        if file_path is None:

            continue

        df = load_unit_data(
            file_path,
            unit=unit
        )

        check_unit_data(
            df
        )

        frames.append(
            df
        )

    if not frames:

        raise FileNotFoundError(
            "No unit CSV files were found.\n\n"
            "Expected files such as:\n"
            "unit1.csv\n"
            "unit2.csv\n"
            "...\n"
            "unit11.csv"
        )

    combined = pd.concat(
        frames,
        ignore_index=True
    )

    combined = combined.sort_values(
        [
            "Student",
            "Unit"
        ]
    )

    combined = combined.reset_index(
        drop=True
    )

    return combined


# ============================================================
# STUDENT / UNIT HELPERS
# ============================================================

def get_available_units(df):
    """
    Return units available in the dataset.
    """

    units = (
        pd.to_numeric(
            df["Unit"],
            errors="coerce"
        )
        .dropna()
        .astype(int)
        .unique()
    )

    return sorted(
        units.tolist()
    )


def get_students(df):
    """
    Return students in natural numerical order.

    Example:

        Student 1
        Student 2
        Student 3
        ...
        Student 17
    """

    students = (
        df["Student"]
        .dropna()
        .unique()
        .tolist()
    )

    def student_number(student):

        digits = "".join(
            character
            for character in str(student)
            if character.isdigit()
        )

        if digits:

            return int(digits)

        return 999999

    return sorted(
        students,
        key=student_number
    )


# ============================================================
# LONGITUDINAL SCORES
# ============================================================

def calculate_longitudinal_scores(df):
    """
    Return Listening and Reading scores for every
    student across Units 1-11.
    """

    check_unit_data(
        df
    )

    columns = [
        "Student",
        "Unit",
        "Listening Total",
        "Reading Total",
    ]

    return (
        df[columns]
        .sort_values(
            [
                "Student",
                "Unit"
            ]
        )
        .reset_index(
            drop=True
        )
    )


# ============================================================
# ERROR DATA
# ============================================================

def calculate_error_longitudinal(df):
    """
    Convert the error data into long format.

    Returns columns:

        Student
        Unit
        Skill
        Error Type
        Errors
    """

    check_unit_data(
        df
    )

    records = []

    for _, row in df.iterrows():

        for skill in SKILLS:

            for error_type in ERROR_TYPES:

                column = (
                    f"{skill} "
                    f"{error_type}"
                )

                records.append({

                    "Student":
                        row["Student"],

                    "Unit":
                        row["Unit"],

                    "Skill":
                        skill,

                    "Error Type":
                        error_type,

                    "Errors":
                        row[column],
                })

    return pd.DataFrame(
        records
    )


# ============================================================
# INDIVIDUAL STUDENT
# ============================================================

def calculate_student_progress(
    df,
    student
):
    """
    Return all available units for one student.
    """

    student_df = df[
        df["Student"] == student
    ].copy()

    return (
        student_df
        .sort_values("Unit")
        .reset_index(drop=True)
    )


def calculate_student_summary(
    df,
    student
):
    """
    Calculate Listening and Reading progress
    for one student.

    Includes:

        First Score
        Final Score
        Score Change
        Mean Score
        Highest Score
        Lowest Score
        Units Completed
    """

    student_df = calculate_student_progress(
        df,
        student
    )

    results = []

    for skill in SKILLS:

        column = f"{skill} Total"

        valid = student_df[
            column
        ].dropna()

        if valid.empty:

            continue

        first_row = student_df[
            student_df[column].notna()
        ].iloc[0]

        final_row = student_df[
            student_df[column].notna()
        ].iloc[-1]

        results.append({

            "Student":
                student,

            "Skill":
                skill,

            "First Unit":
                int(first_row["Unit"]),

            "Final Unit":
                int(final_row["Unit"]),

            "First Score":
                valid.iloc[0],

            "Final Score":
                valid.iloc[-1],

            "Score Change":
                valid.iloc[-1]
                - valid.iloc[0],

            "Mean Score":
                valid.mean(),

            "Highest Score":
                valid.max(),

            "Lowest Score":
                valid.min(),

            "Units Completed":
                valid.count(),
        })

    return pd.DataFrame(
        results
    )


# ============================================================
# ERROR SUMMARY
# ============================================================

def calculate_student_error_summary(
    df,
    student
):
    """
    Calculate first-to-final error change
    for one student.
    """

    student_df = calculate_student_progress(
        df,
        student
    )

    records = []

    for skill in SKILLS:

        for error_type in ERROR_TYPES:

            column = (
                f"{skill} "
                f"{error_type}"
            )

            valid = student_df[
                ["Unit", column]
            ].dropna(
                subset=[column]
            )

            if valid.empty:

                continue

            first = valid.iloc[0][column]
            final = valid.iloc[-1][column]

            records.append({

                "Student":
                    student,

                "Skill":
                    skill,

                "Error Type":
                    error_type,

                "First Unit Errors":
                    first,

                "Final Unit Errors":
                    final,

                "Error Change":
                    final - first,

                "Mean Errors":
                    valid[column].mean(),
            })

    return pd.DataFrame(
        records
    )


# ============================================================
# UNIT STATISTICS
# ============================================================

def calculate_unit_statistics(df):
    """
    Calculate average Listening and Reading
    scores for each unit.
    """

    return (
        df.groupby("Unit")
        .agg(

            Listening_Mean=(
                "Listening Total",
                "mean"
            ),

            Reading_Mean=(
                "Reading Total",
                "mean"
            ),

            Listening_Median=(
                "Listening Total",
                "median"
            ),

            Reading_Median=(
                "Reading Total",
                "median"
            ),

            Students=(
                "Student",
                "nunique"
            ),
        )
        .reset_index()
        .sort_values("Unit")
    )


def calculate_unit_error_statistics(df):
    """
    Calculate average errors by:

        Unit
        Skill
        Error Type
    """

    error_long = (
        calculate_error_longitudinal(
            df
        )
    )

    return (
        error_long
        .groupby(
            [
                "Unit",
                "Skill",
                "Error Type",
            ],
            as_index=False
        )["Errors"]
        .mean()
        .rename(
            columns={
                "Errors":
                    "Mean Errors"
            }
        )
        .sort_values(
            [
                "Unit",
                "Skill",
                "Error Type"
            ]
        )
    )


# ============================================================
# UNIT-TO-UNIT CHANGE
# ============================================================

def calculate_student_unit_change(df):
    """
    Calculate change from each student's
    previous unit.

    Example:

        U1 -> U2
        U2 -> U3
        ...
        U10 -> U11
    """

    data = (
        calculate_longitudinal_scores(
            df
        )
        .copy()
    )

    for skill in SKILLS:

        column = f"{skill} Total"

        data[
            f"{skill} Change"
        ] = (
            data
            .groupby("Student")[column]
            .diff()
        )

    return data


# ============================================================
# ALL STUDENTS
# ============================================================

def calculate_all_student_summaries(df):
    """
    Create Listening and Reading summaries
    for every student.
    """

    frames = []

    for student in get_students(df):

        summary = calculate_student_summary(
            df,
            student
        )

        if not summary.empty:

            frames.append(
                summary
            )

    if not frames:

        return pd.DataFrame()

    return pd.concat(
        frames,
        ignore_index=True
    )


# ============================================================
# REPORT
# ============================================================

def create_longitudinal_report(df):
    """
    Create all major longitudinal analysis tables.
    """

    return {

        "scores":
            calculate_longitudinal_scores(
                df
            ),

        "errors":
            calculate_error_longitudinal(
                df
            ),

        "unit_statistics":
            calculate_unit_statistics(
                df
            ),

        "unit_error_statistics":
            calculate_unit_error_statistics(
                df
            ),

        "student_summaries":
            calculate_all_student_summaries(
                df
            ),

        "unit_changes":
            calculate_student_unit_change(
                df
            ),
    }


# ============================================================
# VISUALIZATION
# ============================================================

def plot_student_scores(
    df,
    student
):
    """
    Plot Listening and Reading scores
    from Unit 1 through Unit 11.
    """

    data = calculate_student_progress(
        df,
        student
    )

    fig, ax = plt.subplots(
        figsize=(11, 5)
    )

    ax.plot(
        data["Unit"],
        data["Listening Total"],
        marker="o",
        label="Listening"
    )

    ax.plot(
        data["Unit"],
        data["Reading Total"],
        marker="o",
        label="Reading"
    )

    ax.set_title(
        f"{student}: Listening and Reading Progress"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Score"
    )

    ax.set_xticks(
        UNITS
    )

    ax.set_ylim(
        0,
        100
    )

    ax.legend()

    ax.grid(
        alpha=0.25
    )

    fig.tight_layout()

    return fig


def plot_student_all_errors(
    df,
    student,
    skill
):
    """
    Plot all four error types for one student
    across Units 1-11.
    """

    if skill not in SKILLS:

        raise ValueError(
            "skill must be Listening or Reading."
        )

    data = calculate_student_progress(
        df,
        student
    )

    fig, ax = plt.subplots(
        figsize=(11, 5)
    )

    for error_type in ERROR_TYPES:

        column = (
            f"{skill} "
            f"{error_type}"
        )

        ax.plot(
            data["Unit"],
            data[column],
            marker="o",
            label=error_type
        )

    ax.set_title(
        f"{student}: {skill} Error Profile"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Number of Errors"
    )

    ax.set_xticks(
        UNITS
    )

    ax.legend()

    ax.grid(
        alpha=0.25
    )

    fig.tight_layout()

    return fig


def plot_student_errors(
    df,
    student,
    skill,
    error_type
):
    """
    Plot one error type for one student.
    """

    if skill not in SKILLS:

        raise ValueError(
            "skill must be Listening or Reading."
        )

    if error_type not in ERROR_TYPES:

        raise ValueError(
            f"Unknown error type: {error_type}"
        )

    data = calculate_student_progress(
        df,
        student
    )

    column = (
        f"{skill} "
        f"{error_type}"
    )

    fig, ax = plt.subplots(
        figsize=(11, 5)
    )

    ax.plot(
        data["Unit"],
        data[column],
        marker="o"
    )

    ax.set_title(
        f"{student}: {skill} — {error_type}"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Number of Errors"
    )

    ax.set_xticks(
        UNITS
    )

    ax.grid(
        alpha=0.25
    )

    fig.tight_layout()

    return fig


def plot_student_total_errors(
    df,
    student
):
    """
    Plot total Listening and Reading errors
    across Units 1-11.
    """

    data = calculate_student_progress(
        df,
        student
    ).copy()

    listening_columns = [
        f"Listening {error}"
        for error in ERROR_TYPES
    ]

    reading_columns = [
        f"Reading {error}"
        for error in ERROR_TYPES
    ]

    data["Listening Errors"] = (
        data[listening_columns]
        .sum(axis=1)
    )

    data["Reading Errors"] = (
        data[reading_columns]
        .sum(axis=1)
    )

    fig, ax = plt.subplots(
        figsize=(11, 5)
    )

    ax.plot(
        data["Unit"],
        data["Listening Errors"],
        marker="o",
        label="Listening Errors"
    )

    ax.plot(
        data["Unit"],
        data["Reading Errors"],
        marker="o",
        label="Reading Errors"
    )

    ax.set_title(
        f"{student}: Total Errors by Unit"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Number of Errors"
    )

    ax.set_xticks(
        UNITS
    )

    ax.legend()

    ax.grid(
        alpha=0.25
    )

    fig.tight_layout()

    return fig


def plot_all_students_scores(
    df,
    skill
):
    """
    Plot one skill for all students
    across Units 1-11.
    """

    if skill not in SKILLS:

        raise ValueError(
            "skill must be Listening or Reading."
        )

    fig, ax = plt.subplots(
        figsize=(12, 7)
    )

    for student in get_students(df):

        data = calculate_student_progress(
            df,
            student
        )

        ax.plot(
            data["Unit"],
            data[f"{skill} Total"],
            marker="o",
            alpha=0.65,
            label=student
        )

    ax.set_title(
        f"All Students: {skill} Progress"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Score"
    )

    ax.set_xticks(
        UNITS
    )

    ax.set_ylim(
        0,
        100
    )

    ax.grid(
        alpha=0.25
    )

    if len(get_students(df)) <= 20:

        ax.legend(
            bbox_to_anchor=(1.02, 1),
            loc="upper left"
        )

    fig.tight_layout()

    return fig


def plot_unit_average_progress(df):
    """
    Plot average Listening and Reading
    scores across Units 1-11.
    """

    stats = calculate_unit_statistics(
        df
    )

    fig, ax = plt.subplots(
        figsize=(11, 5)
    )

    ax.plot(
        stats["Unit"],
        stats["Listening_Mean"],
        marker="o",
        label="Listening Mean"
    )

    ax.plot(
        stats["Unit"],
        stats["Reading_Mean"],
        marker="o",
        label="Reading Mean"
    )

    ax.set_title(
        "Average Listening and Reading Progress"
    )

    ax.set_xlabel(
        "Unit"
    )

    ax.set_ylabel(
        "Mean Score"
    )

    ax.set_xticks(
        UNITS
    )

    ax.set_ylim(
        0,
        100
    )

    ax.legend()

    ax.grid(
        alpha=0.25
    )

    fig.tight_layout()

    return fig
