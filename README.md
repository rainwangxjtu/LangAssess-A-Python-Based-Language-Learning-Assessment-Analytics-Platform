# LangAssess

**Data-Driven Language Learning and Assessment Analytics**

LangAssess is a Python-based analytics platform designed to help language educators track student progress, identify recurring patterns in learner writing, and evaluate consistency across human raters.

The project was developed to address a practical problem in language education: instructional decisions and assessment practices can often rely heavily on individual instructor judgment and manually maintained records. LangAssess brings these data together into a unified workflow for longitudinal analysis, learner-error analysis, and assessment reliability.

## Project Overview

LangAssess currently focuses on three areas:

1. **Student Progress Analytics**

   * Tracks longitudinal assessment data across multiple cohorts.
   * Calculates individual and cohort-level performance metrics.
   * Visualizes student and cohort trajectories over time.
   * Identifies patterns in improvement and decline.

2. **Learner Writing Error Analysis**

   * Categorizes recurring errors in student writing.
   * Measures error frequency across students and cohorts.
   * Incorporates error severity into instructional-priority analysis.
   * Helps identify grammar and language areas that may require additional instructional attention.

3. **Inter-Rater Reliability Analysis**

   * Compares scores assigned by multiple instructors.
   * Calculates exact agreement between raters.
   * Calculates Cohen's kappa for categorical/ordinal ratings.
   * Tracks agreement across assignments and time.
   * Supports before-and-after comparisons following changes to assessment procedures.

## Motivation

In a language-learning environment, instructors generate substantial amounts of assessment and learner-performance data. However, these data are often distributed across spreadsheets, grading records, and individual instructor observations.

This creates several challenges:

* Longitudinal student patterns are difficult to identify manually.
* Common learner errors may not be obvious from individual assignments.
* Instructional priorities can depend heavily on instructor intuition.
* Differences in grading practices can introduce measurement variability.
* Manual analysis becomes increasingly difficult as the number of students and assessments grows.

LangAssess addresses these problems by transforming raw instructional data into reproducible analytical outputs.

## System Architecture

```text
                 ┌─────────────────────┐
                 │   Student Records   │
                 └──────────┬──────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │   Data Cleaning   │
                  │  & Normalization  │
                  └────────┬─────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
       ┌───────────┐ ┌───────────┐ ┌──────────────┐
       │ Progress  │ │  Writing  │ │ Inter-Rater  │
       │ Analytics │ │   Errors  │ │ Reliability  │
       └─────┬─────┘ └─────┬─────┘ └──────┬───────┘
             │             │               │
             └─────────────┼───────────────┘
                           ▼
                  ┌──────────────────┐
                  │    Dashboard     │
                  │  & Visualization │
                  └──────────────────┘
```

## Technology Stack

* **Python**
* **Pandas** — data manipulation and analysis
* **NumPy** — numerical computation
* **Streamlit** — interactive dashboard
* **Matplotlib / Streamlit charts** — visualization
* **Statistical agreement metrics** — inter-rater reliability analysis

Future versions may incorporate:

* scikit-learn
* NLP-based error classification
* sentence embeddings
* automated linguistic feature extraction
* LLM-assisted feedback
* database-backed storage

## Data Model

### Student Progress

```text
student_id
cohort
date
assessment
score
max_score
```

The application converts raw scores into normalized percentages and uses these values to analyze individual and cohort trajectories.

### Writing Errors

```text
student_id
cohort
assignment
error_category
severity
```

Example categories include:

* Word order
* Aspect
* Particles
* Measure words
* Vocabulary
* Sentence structure
* Pronunciation

The system aggregates these categories to identify high-frequency and high-severity error patterns.

### Rater Scores

```text
student_id
assignment
rater_1
rater_2
rater_3
```

The system compares ratings across instructors and calculates agreement metrics.

## Key Metrics

### Student Progress

The dashboard reports:

* Number of students
* Number of cohorts
* Number of assessments
* Mean score
* Median score
* Individual trajectories
* Cohort trajectories

### Writing Analysis

The dashboard reports:

* Error frequency
* Number of students affected
* Average severity
* Error distribution by cohort
* Instructional priority rankings

### Grading Consistency

The dashboard reports:

* Exact agreement
* Pairwise agreement
* Cohen's kappa
* Agreement by assignment
* Agreement before and after an intervention

## Example Workflow

A typical analysis follows this pipeline:

```text
Raw Assessment Data
        ↓
Data Cleaning
        ↓
Score Normalization
        ↓
Longitudinal Analysis
        ↓
Cohort Comparison
        ↓
Visualization
```

For learner writing:

```text
Student Writing
        ↓
Error Annotation
        ↓
Error Categorization
        ↓
Frequency + Severity Analysis
        ↓
Instructional Priorities
```

For assessment reliability:

```text
Multiple Instructor Ratings
        ↓
Pairwise Comparison
        ↓
Agreement Metrics
        ↓
Before / After Analysis
        ↓
Assessment Reliability Evaluation
```

## Results

In the original instructional use case, the workflow was applied to approximately **68 students across three cohorts**.

The system was used to:

* consolidate student performance data,
* identify recurring learner-error patterns,
* support instructional prioritization, and
* monitor consistency among instructors.

Following implementation of a revised grading-consistency workflow, scoring agreement across raters improved by approximately **25%**.

> The reported improvement should be calculated from documented pre- and post-intervention data rather than treated as a hard-coded result.

## Example Dashboard

The planned dashboard provides views such as:

```text
┌──────────────────────────────────────────────┐
│              LANGASSESS                      │
├────────────┬────────────┬────────────────────┤
│ Students   │ Cohorts    │ Average Score      │
│    68      │     3      │      87.4%         │
├────────────┴────────────┴────────────────────┤
│                                              │
│          Student Progress Over Time          │
│                 📈                           │
│                                              │
├──────────────────────────────────────────────┤
│              Writing Errors                  │
│                                              │
│ Word Order       █████████████                │
│ Aspect           ██████████                   │
│ Particles        ████████                     │
│ Measure Words    ██████                       │
│                                              │
├──────────────────────────────────────────────┤
│          Inter-Rater Agreement               │
│                                              │
│ Before: 64.2%                                │
│ After:  80.1%                                │
│ Improvement: 24.8%                           │
└──────────────────────────────────────────────┘
```

*Values shown above are illustrative and are not intended to represent actual program results.*

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/lang-assess.git
cd lang-assess
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The dashboard will open locally at:

```text
http://localhost:8501
```

## Project Structure

```text
lang-assess/
│
├── app.py
├── data/
│   ├── progress.csv
│   ├── writing_errors.csv
│   └── ratings.csv
│
├── analysis/
│   ├── progress.py
│   ├── writing_errors.py
│   └── agreement.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Data Privacy

This project is designed to work with educational data, which may contain sensitive student information.

Real student data should **not** be committed to a public GitHub repository.

For demonstration purposes, this repository uses synthetic or anonymized data.

Before using the system with real student records, users should follow applicable institutional privacy, data-security, and records-management requirements.

## Future Development

Planned improvements include:

* Automated linguistic error detection
* NLP-based learner-error classification
* Student risk/trajectory detection
* More sophisticated inter-rater reliability statistics
* Interactive filtering by cohort and assessment
* Database integration
* Automated reporting
* LLM-assisted feedback with structured output validation

## Author

**Yuqi Wang**

Language and Linguistics | Python | NLP | Data Analytics

This project represents an application of software engineering and data analysis to problems in language education and assessment.
