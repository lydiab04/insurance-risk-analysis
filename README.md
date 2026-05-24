# Insurance Risk Analytics for ACIS

## Project Overview

This project was developed for AlphaCare Insurance Solutions (ACIS) to support data-driven insurance pricing, customer segmentation, and marketing optimization. The project analyzes historical vehicle insurance data to uncover profitability drivers, identify high-risk customer groups, and establish the foundation for predictive risk modeling.

The work combines:
- Exploratory Data Analysis (EDA)
- Data Version Control (DVC)
- Statistical hypothesis testing
- Machine learning modeling
- Explainable AI techniques

The ultimate goal is to help ACIS improve underwriting decisions and develop a dynamic risk-based pricing strategy.

---

# Business Problem

ACIS is preparing for aggressive growth within the insurance market and requires evidence-based methods to:
- optimize marketing investments,
- improve premium pricing accuracy,
- identify low-risk customer segments,
- and reduce portfolio loss ratios.

Traditional pricing approaches often rely on generalized assumptions. This project introduces analytics-driven decision making using historical claims and policy data.

---

# Project Objectives

The project is divided into four major tasks:

## Task 1 — Exploratory Data Analysis (EDA)
- Analyze portfolio profitability
- Evaluate claim severity and frequency
- Identify geographic and vehicle-related risk patterns
- Detect outliers and temporal trends

## Task 2 — Data Version Control (DVC)
- Track dataset versions
- Ensure reproducibility
- Create auditable data pipelines

## Task 3 — Statistical Hypothesis Testing
- Validate risk differences across:
  - provinces,
  - zip codes,
  - gender,
  - and profitability groups

## Task 4 — Predictive Modeling
- Predict claim severity
- Predict claim probability
- Build a dynamic premium optimization framework
- Apply SHAP interpretability analysis

---

# Dataset Overview

The dataset contains:
- customer demographics,
- policy information,
- geographic attributes,
- vehicle characteristics,
- premium values,
- and claims data.

### Dataset Size

- **Rows:** 10,000
- **Columns:** 21

### Key Features

| Category | Example Features |
|---|---|
| Customer | Age, Gender, AnnualIncome |
| Geography | Province, ZipCode |
| Vehicle | VehicleType, AutoMake, VehicleModel |
| Risk | RiskScore, PastClaims |
| Financial | TotalPremium, TotalClaims, ClaimAmount |

---

# Key Business Metrics

## Loss Ratio

```text
Loss Ratio = TotalClaims / TotalPremium
```

Measures underwriting profitability.

## Margin

```text
Margin = TotalPremium − TotalClaims
```

Measures insurer profit contribution per policy.

---

# Project Structure

```text
insurance-risk-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── insurance_data.csv.dvc
│   └── insurance_data_cleaned.csv.dvc
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
│
├── reports/
│   ├── interim_report.md
│   └── final_report.md
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
│
├── tests/
│   └── test_basic.py
│
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# Technologies Used

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Explainability | SHAP |
| Testing | Pytest |
| Linting | Flake8 |
| CI/CD | GitHub Actions |
| Version Control | Git + DVC |

---

# Installation

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd insurance-risk-analytics
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks directory and run:
- `01_eda.ipynb`
- `02_hypothesis_testing.ipynb`
- `03_modeling.ipynb`

---

# Data Version Control (DVC)

This project uses DVC to ensure reproducible and auditable dataset management.

## Pull Dataset

```bash
dvc pull
```

## Track New Dataset

```bash
dvc add data/insurance_data.csv
```

## Push Dataset to Remote Storage

```bash
dvc push
```

---

# Continuous Integration (CI/CD)

GitHub Actions is configured to automatically:

- install dependencies,
- run linting using `flake8`,
- execute tests using `pytest`.

The workflow runs automatically on:
- pushes,
- pull requests,
- and branch merges.

---

# Exploratory Data Analysis Highlights

Key findings from the exploratory analysis include:

- Significant geographic variation in loss ratios
- Heavy-tailed claim severity distributions
- Strong relationships between risk scores and premiums
- Vehicle-specific claim severity patterns
- Seasonal fluctuations in claims activity

---

# Planned Statistical Analysis

Future phases of the project will include:

- A/B hypothesis testing
- Chi-squared tests
- T-tests and ANOVA
- Claim frequency analysis
- Profitability segmentation

---

# Planned Machine Learning Models

## Regression Models
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

## Classification Models
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

## Interpretability
- SHAP analysis
- Feature importance evaluation

---

# Contributors

Developed as part of the Insurance Risk Analytics project for AlphaCare Insurance Solutions (ACIS).

---

# License

This project is for academic and educational purposes.
