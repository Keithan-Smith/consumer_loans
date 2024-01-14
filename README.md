# Credit Risk Analysis Project

## Project Overview
This project focuses on a binary classification problem in the context of credit risk analysis. Using a dataset where each entry represents an individual taking credit from a bank, the goal is to predict the `loan_status` (0 or 1), indicating whether the individual will default on the loan.

### Key Details of the Dataset:
- **Target Variable**: `loan_status`
  - 1: Default on loan.
  - 0: No default.
- **Nature of the Problem**: Binary classification.
- **Imbalance in Data**: The dataset is highly imbalanced.
- **Features**:
  - `person_age`: Age of the person (numerical).
  - `person_income`: Annual income (numerical).
  - `person_home_ownership`: Home ownership status ('MORTGAGE', 'RENT', 'OWN', 'OTHER').
  - `person_emp_length`: Employment length in years (numerical).
  - `loan_intent`: Purpose of the loan ('VENTURE', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'EDUCATION', 'PERSONAL').
  - `loan_grade`: Loan grade ('A', 'C', 'D', 'B', 'E', 'F', 'G').
  - `loan_amnt`: Loan amount (numerical).
  - `loan_int_rate`: Loan interest rate (numerical).
  - `loan_percent_income`: Loan as a percentage of income (numerical).
  - `cb_person_default_on_file`: Historical default ('N', 'Y').
  - `cb_person_cred_hist_length`: Credit history length (numerical).

## Setup Instructions
To ensure the project runs smoothly on your machine, follow these steps:

### 1. Clone the Repository
Clone this repository to your local machine using your preferred method (SSH or HTTPS).

### 2. Navigate to the Project Directory
Open a command line interface and navigate to the root directory of the project.

### 3. Set Up a Python Virtual Environment (Optional but Recommended)
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment:
  - Windows: `.\venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`

### 4. Run the Setup Script
Execute the following command to install all required dependencies:
- `python setup.py`
