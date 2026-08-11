# LangAccess

### Longitudinal Student Progress & Error Analysis Platform

LangAccess is a Python-based analytics platform for tracking **individual student progress across multiple assessment units** and analyzing recurring error patterns over time.

The system transforms assessment data into longitudinal performance trajectories, error-type distributions, and student-level progress reports. It is designed to support data-driven instructional decisions while providing a reproducible framework for analyzing learner performance.

---

## Overview

Traditional assessment records often capture scores for individual assignments but make it difficult to answer longitudinal questions such as:

* How is an individual student's performance changing across units?
* Which error types persist over time?
* Is a student's overall score improving because of genuine improvement or changes in specific skill areas?
* Which linguistic error categories contribute most to performance difficulties?
* How can assessment data be transformed into interpretable progress reports?

**LangAccess** addresses these questions by organizing assessment data into a consistent longitudinal structure and automatically generating analyses of both **performance** and **error patterns**.

---

## Key Features

### 📈 Longitudinal Progress Tracking

Track individual students from **Unit 1 through Unit 11**, allowing performance trajectories to be examined across an extended curriculum.

The system supports:

* Listening performance
* Reading performance
* Speaking performance
* Unit-level total scores
* Student-level progress trajectories
* Cross-unit change analysis

### 🔎 Error-Type Analysis

Listening and Reading assessments are analyzed using four structured error categories:

1. **Grammar**
2. **Vocabulary Retention**
3. **Discourse Analysis**
4. **Sociocultural Background Knowledge**

LangAccess aggregates these categories across units to identify recurring weaknesses and changing error distributions.

### 👤 Individual Student Profiles

Rather than focusing only on cohort averages, LangAccess prioritizes **individual longitudinal profiles**.

For each student, the system can identify:

* Overall score trends
* Persistent error categories
* Improving error categories
* Units with significant performance changes
* Relative strengths and weaknesses

### 📊 Automated Visualization

The analysis pipeline generates visualizations that make longitudinal patterns easier to interpret, including:

* Unit-by-unit progress trajectories
* Listening and Reading performance trends
* Error-type distributions
* Error-type trends across units
* Student-level comparisons across assessment dimensions

### ⚙️ Reproducible Data Pipeline

Assessment data can be processed using a consistent workflow rather than manually calculating scores or constructing charts.

The pipeline is designed to:

* Validate expected columns
* Parse unit-level assessment data
* Aggregate error categories
* Calculate longitudinal metrics
* Generate student-level reports
* Produce standardized visualizations

---

## Data Structure

LangAccess is designed around a repeated assessment structure in which each curriculum unit contains the same set of assessment variables.

A simplified representation is:

```text
Unit 1
├── Listening
│   ├── Total
│   ├── Grammar
│   ├── Vocabulary Retention
│   ├── Discourse Analysis
│   └── Sociocultural Background Knowledge
│
├── Reading
│   ├── Total
│   ├── Grammar
│   ├── Vocabulary Retention
│   ├── Discourse Analysis
│   └── Sociocultural Background Knowledge
│
└── Speaking
    └── Total

Unit 2
├── Listening
├── Reading
└── Speaking

...

Unit 11
├── Listening
├── Reading
└── Speaking
```

This consistent schema allows the same analytical procedures to be applied across the entire curriculum.

---

## Example Analysis

For a student with Listening performance across multiple units:

```text
Unit        Listening Score
--------------------------------
Unit 1          72.5
Unit 2          75.0
Unit 3          78.5
Unit 4          81.0
Unit 5          84.0
...
Unit 11         91.5
```

LangAccess can additionally examine the underlying error distribution:

```text
Error Type                  Unit 1    Unit 6    Unit 11
---------------------------------------------------------
Grammar                       High      Medium     Low
Vocabulary Retention         High      Medium     Low
Discourse Analysis           Medium    Medium     Low
Sociocultural Knowledge      Medium    Low        Low
```

This makes it possible to distinguish between **overall score improvement** and **improvement in specific error categories**.

---

## Project Architecture

The project follows a modular analysis workflow:

```text
                 Assessment Data
                       │
                       ▼
              ┌─────────────────┐
              │ Data Validation  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Data Processing │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
       Score Analysis      Error Analysis
              │                 │
              ▼                 ▼
       Progress Trends     Error Trends
              │                 │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Visualization & │
              │     Reports     │
              └─────────────────┘
```

---

## Technology Stack

* **Python**
* **pandas** — tabular data processing and aggregation
* **NumPy** — numerical analysis
* **Matplotlib** — data visualization
* **CSV / tabular datasets** — assessment data storage
* **Git / GitHub** — version control and reproducibility

---

## Example Workflow

### 1. Prepare assessment data

Assessment files follow a standardized unit-level schema.

```text
data/
├── unit01.csv
├── unit02.csv
├── unit03.csv
├── ...
└── unit11.csv
```

### 2. Run the analysis

```bash
python progress.py
```

### 3. Generate outputs

The pipeline produces student-level longitudinal analyses and visualizations.

Example output structure:

```text
outputs/
├── student_progress/
│   ├── student_01_progress.png
│   ├── student_02_progress.png
│   └── ...
│
├── error_analysis/
│   ├── student_01_errors.png
│   ├── student_02_errors.png
│   └── ...
│
└── summary/
    └── progress_summary.csv
```

---

## Design Principles

### Individual Progress Over Cohort Averages

The primary unit of analysis is the **individual student**.

Cohort-level summaries can hide important variation between learners. LangAccess therefore emphasizes student-specific trajectories and error patterns.

### Performance + Error Analysis

A single score does not explain *why* performance changes.

LangAccess combines:

```text
Performance
     +
Error Categories
     +
Longitudinal Trends
     ↓
More Interpretable Student Profiles
```

### Reproducibility

The same analytical workflow can be applied to new assessment units without manually rebuilding calculations or visualizations.

### Extensibility

The modular design allows additional assessment dimensions, error categories, and analytical metrics to be incorporated as the project evolves.

---

## Potential Applications

Although developed for language-learning assessment, the underlying framework can be generalized to other longitudinal educational datasets.

Potential applications include:

* Language proficiency assessment
* Formative assessment
* Learning analytics
* Error analysis
* Individualized instruction
* Longitudinal educational research
* Student performance monitoring

---

## Project Motivation

LangAccess was developed from a practical need to transform repeated language assessments into **actionable longitudinal data**.

Rather than treating each assessment as an isolated score, the project treats student performance as a time series and examines both **what changes** and **which underlying error patterns drive those changes**.

The broader goal is to connect educational assessment with computational analysis, enabling instructors and researchers to make more systematic use of learner data.

---

## Future Development

Potential future improvements include:

* Interactive dashboards
* Automated PDF/HTML student reports
* Statistical significance testing for longitudinal changes
* Automated anomaly detection
* Error-type prediction
* LLM-assisted qualitative error analysis
* Database-backed assessment storage
* Web-based instructor interface
* Integration with additional assessment modalities

---

## Privacy & Data Protection

This repository is designed to operate on **de-identified or synthetic assessment data**.

No personally identifiable student information should be committed to the repository.

For real-world deployments, appropriate institutional data-protection requirements should be followed.

---

## Author

**Yuqi Wang**

Assistant Professor (Language and Linguistics), Defense Language Institute

Interests include:

* Natural Language Processing
* Language Intelligence
* Learning Analytics
* Computational Linguistics
* AI-assisted Language Assessment
* Data-driven Educational Technology

---

## License

This project is intended for research and educational purposes.
