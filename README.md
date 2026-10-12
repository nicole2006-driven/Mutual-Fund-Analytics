# Mutual Fund Analytics

A Python-based Mutual Fund Analytics Capstone Project focused on data ingestion, NAV retrieval, data exploration, and data quality validation.

## Project Objectives

- Load and inspect 10 mutual fund datasets using Pandas.
- Fetch mutual fund NAV data using the MFAPI API.
- Explore fund houses, categories, sub-categories, and risk classifications.
- Validate AMFI scheme codes across Fund Master and NAV History datasets.
- Generate data quality reports.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- Requests
- SciPy
- Jupyter
- Git and GitHub

## Project Structure

```text
Mutual-Fund-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│   └── day1_data_quality_report.md
├── data_ingestion.py
├── live_nav_fetch.py
├── fund_master_exploration.py
├── amfi_validation.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Day 1: Data Ingestion

### 1. Dataset Loading

Loaded and inspected 10 CSV datasets using Pandas, including dataset shapes, data types, sample records, missing values, and duplicate records.

### 2. Live NAV Retrieval

Retrieved NAV data from MFAPI for six mutual fund schemes, including HDFC Top 100, SBI Bluechip, ICICI Bluechip, Nippon Large Cap, Axis Bluechip, and Kotak Bluechip.

API: https://api.mfapi.in/

### 3. Fund Master Exploration

Explored mutual fund houses, categories, sub-categories, risk classifications, and AMFI scheme codes.

### 4. AMFI Code Validation

- Fund Master Records: 40
- NAV History Records: 46,000
- Matching AMFI Codes: 40
- Missing AMFI Codes: 0
- Duplicate Fund Master Codes: 0
- Duplicate NAV Scheme-Date Records: 0
- AMFI Code Coverage: **100%**

**Validation Result: PASS**

## Dataset Availability and Privacy

The 10 CSV datasets used in this project were provided as part of an internship capstone assignment.

These datasets are intentionally excluded from this public GitHub repository because redistribution permission has not yet been confirmed.

The original datasets are retained locally for development and analysis. Generated CSV files and CSV-based reports are also excluded from version control pending review.

The source code, dependency list, methodology, and non-sensitive summary documentation are available publicly.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/Mutual-Fund-Analytics.git
cd Mutual-Fund-Analytics
python -m venv .venv
```

Activate the virtual environment on Windows:

```cmd
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Project

After placing the authorized input datasets inside `data/raw/`, run:

```bash
python data_ingestion.py
python live_nav_fetch.py
python fund_master_exploration.py
python amfi_validation.py
```

The live NAV fetching script uses publicly accessible MFAPI endpoints. The remaining data analysis scripts require the corresponding local CSV datasets.

## Project Status

**Day 1 — Data Ingestion: Completed**

## Future Scope

- Data cleaning and preprocessing
- SQL-based mutual fund analysis
- Performance and risk analytics
- Interactive dashboards
- Automated reporting