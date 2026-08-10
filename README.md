# LangAssess: Language Learning Assessment Analytics Platform

## Overview

**LangAssess** is a Python-based assessment analytics platform designed to help language educators analyze student performance, identify learning patterns, and make more data-informed instructional decisions.

The project demonstrates how Python and data analysis can transform student assessment data from individual observations into structured, longitudinal insights.

The current demonstration version analyzes **17 students across three cohorts** and provides interactive tools for examining grade trajectories, progress patterns, and assessment outcomes.

---

## Motivation

Language instructors often evaluate student progress using a combination of grades, written work, classroom observations, and professional judgment.

While these sources are valuable, relying primarily on individual observations can make it difficult to:

* identify long-term performance trends
* compare progress across cohorts
* detect students whose performance is changing
* summarize large amounts of assessment data
* make consistent, evidence-based decisions

LangAssess addresses this problem by organizing assessment information into a structured dataset and using Python-based analytics to identify patterns that may not be immediately visible from individual records.

---

## Project Goals

The main goals of LangAssess are to:

1. Track student performance over time.
2. Compare progress across multiple cohorts.
3. Identify patterns in student grades and assessment outcomes.
4. Provide educators with interpretable visualizations and summaries.
5. Demonstrate how Python can support language assessment and instructional decision-making.

---

## Current Version

The current demo uses:

* **17 students**
* **3 cohorts**
* Longitudinal assessment data
* Student-level progress tracking
* Cohort-level comparisons
* Interactive Streamlit visualizations

The dataset is intentionally small so that the project can be easily understood, tested, and demonstrated while preserving the structure needed to scale to larger datasets.

---

## Key Features

### 1. Progress Analytics

The progress analytics module organizes student assessment data and calculates performance trends over time.

It can be used to examine:

* individual student trajectories
* average performance
* assessment changes
* cohort-level performance
* students showing improvement or decline

The goal is to move beyond looking at a single grade and instead examine **performance as a trajectory**.

---

### 2. Cohort Comparison

Students are organized into three cohorts, allowing the application to compare groups rather than analyzing every student independently.

Cohort-level analysis can help answer questions such as:

* Which cohort has the highest average performance?
* How does performance change over time?
* Are some cohorts improving faster than others?
* Which assessment periods show the largest changes?

---

### 3. Student-Level Analysis

LangAssess allows individual students to be examined separately.

For each student, the application can provide a longitudinal view of their assessment performance.

This makes it possible to identify patterns such as:

* consistent improvement
* stable performance
* gradual decline
* sudden changes in performance
* differences between students within the same cohort

---

### 4. Data-Driven Decision Support

The purpose of the application is not to replace instructor judgment.

Instead, it provides an additional layer of evidence that can support professional judgment.

Rather than asking only:

> "What do I remember about this student's performance?"

the system encourages questions such as:

> "What does the student's performance data show over time?"

This distinction is particularly important when working with multiple students and cohorts.

---

## Technology Stack

The project is built primarily with Python.

### Core Technologies

* **Python**
* **Pandas** — data manipulation and analysis
* **NumPy** — numerical computation
* **Streamlit** — interactive web application
* **Matplotlib / Plotly** — data visualization
* **Git / GitHub** — version control and project management

---

## Project Structure

```text
lang-assess/
│
├── app.py
│
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
│
└── README.txt
```

---

## Data

The project separates data from analysis code so that the analytical workflow can be modified without changing the underlying application structure.

### `progress.csv`

Contains longitudinal student assessment information used for progress analysis.

Example fields may include:

```text
student_id
cohort
assessment
score
```

### `writing_errors.csv`

Contains structured information about learner writing errors.

This module is designed to support analysis of error patterns and linguistic features.

### `ratings.csv`

Contains assessment ratings used to examine agreement between evaluators.

---

## Analytical Modules

The project is designed around three analytical components.

### Progress Analytics

Examines longitudinal student performance and cohort-level trends.

### Writing Error Analysis

Organizes learner writing errors into structured categories so that recurring linguistic patterns can be analyzed.

### Inter-Rater Reliability

Provides a framework for examining consistency between different evaluators.

Together, these components demonstrate how assessment data can be analyzed at multiple levels:

```text
Student Level
      ↓
Assessment Level
      ↓
Cohort Level
      ↓
Program-Level Insights
```

---

## Example Workflow

A typical workflow looks like this:

```text
Assessment Data
      ↓
Data Cleaning
      ↓
Data Organization
      ↓
Statistical Analysis
      ↓
Visualization
      ↓
Pattern Identification
      ↓
Instructional Decision Support
```

For example, an instructor could use the system to identify a student whose scores have declined across several assessments, then examine the student's writing-error profile to determine whether a particular linguistic feature may be contributing to the change.

---

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/lang-assess.git
cd lang-assess
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Example Questions the Application Can Help Answer

LangAssess is designed around practical assessment questions such as:

### Individual Student

* Is this student's performance improving?
* Has the student's performance changed significantly over time?
* Which assessments show the largest changes?

### Cohort

* How do the three cohorts compare?
* Which cohort has the strongest average performance?
* Are performance trends consistent across cohorts?

### Assessment

* Which assessments produce the largest score differences?
* Are certain assessment periods associated with declines or improvements?

### Instruction

* Which students may benefit from additional attention?
* Are certain error categories appearing repeatedly?
* Are assessment decisions consistent across evaluators?

---

## Why Python?

Python provides a practical environment for combining data processing, statistical analysis, visualization, and machine learning.

For this project, Python makes it possible to move through the complete analytical workflow:

```text
Raw Data
   ↓
Pandas
   ↓
Analysis
   ↓
Visualization
   ↓
Interpretation
```

This workflow can eventually be extended to larger datasets and more advanced NLP or machine-learning models.

---

## Scalability

Although the current demonstration contains 17 students across three cohorts, the architecture is designed to scale.

The same workflow can be applied to larger datasets containing:

* additional students
* additional cohorts
* more assessment periods
* additional linguistic features
* larger collections of learner writing
* multiple evaluators

The smaller dataset makes the project easier to demonstrate while maintaining a realistic analytical structure.

---

## Future Development

Potential future extensions include:

* automated longitudinal trend detection
* statistical significance testing
* additional learner-writing analytics
* automated linguistic error classification
* NLP-based feedback generation
* machine-learning-based performance prediction
* interactive student profiles
* additional inter-rater reliability statistics
* database integration
* deployment as a production web application

The long-term goal is to develop LangAssess into a more comprehensive platform for **language assessment analytics and intelligent instructional decision support**.

---

## Privacy and Data Protection

The demonstration dataset is intended for educational and software-development purposes.

Real student information should not be uploaded to a public repository without appropriate authorization.

When working with real assessment data:

* remove personally identifiable information
* use anonymized student identifiers
* follow institutional data-handling policies
* avoid committing sensitive student records to GitHub

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Python programming
* Object-oriented and modular programming
* Data structures
* Pandas data analysis
* Numerical computation
* Data visualization
* Longitudinal data analysis
* Educational data analytics
* Statistical reasoning
* Streamlit application development
* Git and GitHub
* Software project organization

It also demonstrates the ability to connect **domain expertise in language education and linguistics with computational data analysis**.

---

## Author

**Rain Wang**

Assistant Professor (Language and Linguistics)

This project combines language assessment experience with Python-based data analysis to explore how computational methods can support more systematic and evidence-based approaches to language education.

---

## License

This project is intended primarily as an educational and portfolio project.

Add an appropriate open-source license if the repository will be distributed publicly.
