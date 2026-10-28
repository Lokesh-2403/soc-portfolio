# SOC Analyst Portfolio

A cybersecurity project covering detection rule testing and incident response using synthetic authentication logs and a simulated exposed API credential.

## Assessment Tasks

### Task 9: Test a Defensive Detection Rule

**Objective:** Test a detection rule against synthetic authentication logs and identify its limitations.

**Files:**
- `generate_logs.py` — generates synthetic authentication events.
- `logs/auth_logs.csv` — contains the generated events.
- `rules/rule_v1.yml` — Sigma rule for detecting Windows failed logons.

**Testing goals:**
- Identify events that trigger the rule.
- Examine false positives and missed attack scenarios.
- Recommend improvements to the detection rule.

**Test results**: See results/test_results.md for measured results, performance metrics, false positives, missed cases, and improvement recommendations.

### Task 22: The Secret Accidentally Published

**Objective:** Assess the exposure of a possible API credential in a public repository and recommend an incident response.

**Deliverable:** `incident_response.md`

The report covers credential revocation, investigation, verification, and preventive measures.

## Project Structure

```text
soc-portfolio/
├── .gitignore
├── README.md
├── task9-detection-rule/
│   ├── generate_logs.py
│   ├── logs/
│   │   └── auth_logs.csv
│   ├── rules/
│   │   └── rule_v1.yml
│   └── results/
└── task22-leaked-secret/
    └── incident_response.md
```

## Requirements

- Python
- pandas
- PyYAML
- Sigma CLI

## Setup and Run

Clone the repository and enter the project directory:

```powershell
git clone https://github.com/Lokesh-2403/soc-portfolio.git
cd soc-portfolio
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install pandas pyyaml sigma-cli
```

Generate the synthetic authentication logs:

```powershell
python task9-detection-rule\generate_logs.py
```

Validate the Sigma rule:

```powershell
sigma check task9-detection-rule\rules\rule_v1.yml
```

## Disclaimer

This project is for educational and defensive cybersecurity purposes. The authentication logs are synthetic and do not represent real security incidents.

## Author

Lokesh — Aspiring SOC Analyst
