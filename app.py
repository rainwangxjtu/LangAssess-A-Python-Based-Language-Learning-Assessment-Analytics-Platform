"""
app.py

Streamlit dashboard for Unit 1-11
Listening and Reading progress.

Run:

    streamlit run app.py
"""

from pathlib import Path

import streamlit as st

from progress import (
    ERROR_TYPES,
    SKILLS,
    get_students,
    get_available_units,
    load_all_units,
    calculate_student_summary,
    calculate_student_error_summary,
    calculate_student_progress,
    create_longitudinal_report,
    plot_student_scores,
    plot_student_all_errors,
    plot_student_errors,
    plot_student_total_errors,
    plot_all_students_scores,
    plot_unit_average_progress,
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="Unit 1–11 Student Progress",
    page_icon="📈",
    layout="wide",
)

st.title(
    "Unit 1–11 Listening & Reading Progress Tracker"
)

st.caption(
    "Individual longitudinal progress across "
    "Units 1–11. Speaking and Weekly Journal "
    "data are excluded."
)


# ============================================================
# DATA LOCATION
# ============================================================

DATA_FOLDER = Path(
    __file__
).parent


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = load_all_units(
        DATA_FOLDER
    )

except FileNotFoundError as error:

    st.error(
        str(error)
    )

    st.info(
        "Put unit1.csv, unit2.csv, ... "
        "unit11.csv in the same folder as app.py."
    )

    st.stop()

except Exception as error:

    st.error(
        f"Could not load the data: {error}"
    )

    st.stop()


students = get_students(
    df
)

available_units = get_available_units(
    df
)

report = create_longitudinal_report(
    df
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Student Selection"
)

selected_student = st.sidebar.selectbox(
    "Select Student",
    students
)

st.sidebar.markdown(
    "---"
)

st.sidebar.write(
    f"**Students:** {len(students)}"
)

st.sidebar.write(
    f"**Units loaded:** {len(available_units)}"
)

st.sidebar.write(
    "**Focus:** Listening + Reading"
)


# ============================================================
# OVERVIEW
# ============================================================

st.header(
    "Class Overview"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Students",
        len(students)
    )

with col2:

    st.metric(
        "Units Loaded",
        len(available_units)
    )

with col3:

    st.metric(
        "First Unit",
        min(available_units)
    )

with col4:

    st.metric(
        "Latest Unit",
        max(available_units)
    )


# ============================================================
# SELECTED STUDENT
# ============================================================

st.header(
    f"{selected_student}"
)

summary = calculate_student_summary(
    df,
    selected_student
)

if not summary.empty:

    st.subheader(
        "Overall Progress Summary"
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.subheader(
        "Listening and Reading Scores: U1–U11"
    )

    st.pyplot(
        plot_student_scores(
            df,
            selected_student
        ),
        clear_figure=True
    )


# ============================================================
# UNIT-BY-UNIT SCORES
# ============================================================

st.subheader(
    "Unit-by-Unit Scores"
)

student_progress = calculate_student_progress(
    df,
    selected_student
)

score_columns = [
    "Unit",
    "Listening Total",
    "Reading Total",
]

st.dataframe(
    student_progress[
        score_columns
    ],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# ERROR SUMMARY
# ============================================================

st.header(
    f"{selected_student} — Error Analysis"
)

error_summary = calculate_student_error_summary(
    df,
    selected_student
)

st.dataframe(
    error_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# LISTENING ERRORS
# ============================================================

st.subheader(
    "Listening Error Types: U1–U11"
)

st.pyplot(
    plot_student_all_errors(
        df,
        selected_student,
        "Listening"
    ),
    clear_figure=True
)


# ============================================================
# READING ERRORS
# ============================================================

st.subheader(
    "Reading Error Types: U1–U11"
)

st.pyplot(
    plot_student_all_errors(
        df,
        selected_student,
        "Reading"
    ),
    clear_figure=True
)


# ============================================================
# TOTAL ERRORS
# ============================================================

st.subheader(
    "Total Listening vs. Reading Errors"
)

st.pyplot(
    plot_student_total_errors(
        df,
        selected_student
    ),
    clear_figure=True
)


# ============================================================
# INDIVIDUAL ERROR TYPE
# ============================================================

st.header(
    "Individual Error-Type Trend"
)

col1, col2 = st.columns(2)

with col1:

    selected_skill = st.selectbox(
        "Skill",
        SKILLS
    )

with col2:

    selected_error = st.selectbox(
        "Error Type",
        ERROR_TYPES
    )

st.pyplot(
    plot_student_errors(
        df,
        selected_student,
        selected_skill,
        selected_error
    ),
    clear_figure=True
)


# ============================================================
# ALL STUDENTS
# ============================================================

st.header(
    "All Students"
)

st.subheader(
    "Listening Progress"
)

st.pyplot(
    plot_all_students_scores(
        df,
        "Listening"
    ),
    clear_figure=True
)

st.subheader(
    "Reading Progress"
)

st.pyplot(
    plot_all_students_scores(
        df,
        "Reading"
    ),
    clear_figure=True
)


# ============================================================
# UNIT AVERAGES
# ============================================================

st.header(
    "Average Progress Across Units"
)

st.pyplot(
    plot_unit_average_progress(
        df
    ),
    clear_figure=True
)


# ============================================================
# DATA
# ============================================================

with st.expander(
    "View Complete Combined Dataset"
):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DOWNLOAD
# ============================================================

st.header(
    "Download Student Data"
)

csv_data = (
    student_progress
    .to_csv(
        index=False
    )
    .encode("utf-8")
)

st.download_button(
    label="Download Selected Student's Progress",
    data=csv_data,
    file_name=(
        f"{selected_student}_progress.csv"
    ),
    mime="text/csv",
)
