# SOC Analyst Portfolio

A hands-on cybersecurity project focused on authentication log analysis, Sigma detection engineering, and evaluating detection accuracy using synthetic Windows-style security events.

## Project Objectives

- Generate synthetic authentication logs for security analysis.
- Represent successful and failed logons using Windows Event IDs 4624 and 4625.
- Simulate normal authentication activity and password-spraying scenarios.
- Develop Sigma detection rules.
- Evaluate detection performance using true positives, false positives, and missed attacks.
- Document detection limitations and opportunities for improvement.

## Technology Stack

- Python
- CSV
- pandas
- PyYAML
- Sigma CLI
- Git and GitHub

## Project Structure

```text
soc-portfolio/
├── .gitignore
├── README.md
└── task9-detection-rule/
    ├── generate_logs.py
    ├── logs/
    │   └── auth_logs.csv
    ├── rules/
    └── results/
```

## Synthetic Dataset

The current dataset contains 266 generated authentication events.

| Metric | Count |
|---|---:|
| Total events | 266 |
| Attack-labelled events | 47 |
| Benign events | 219 |
| Failed logons (4625) | 114 |
| Successful logons (4624) | 152 |

All events are synthetic and generated for educational purposes. They are not collected from real systems.

## Simulated Scenarios

- Normal successful logons
- Occasional mistyped passwords
- Multiple users sharing a VPN/NAT IP
- Repeated failures from a service account
- A single user's repeated authentication failures
- Loud password spraying
- Low-and-slow password spraying

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd soc-portfolio
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install pandas pyyaml sigma-cli
```

### 4. Generate the authentication logs

```powershell
python task9-detection-rule\generate_logs.py
```

The generated CSV is saved to:

`task9-detection-rule/logs/auth_logs.csv`

## Detection Engineering

The project is being developed in stages:

1. Generate labelled synthetic authentication data.
2. Create a baseline Sigma rule.
3. Evaluate detections against the known scenario labels.
4. Measure precision, recall, false positives, and missed attacks.
5. Refine detection logic and document its limitations.

The initial failed-logon rule is a baseline, not a complete password-spray detector. Detection quality will be assessed through testing rather than assumed.

## Learning Outcomes

- Authentication log analysis
- Basic detection engineering
- Sigma rule development
- Security alert evaluation
- False-positive and false-negative analysis
- Python scripting for security operations
- Git-based project documentation

## Disclaimer

This project is for educational and defensive cybersecurity purposes. It uses synthetic data and does not perform attacks against real systems.

## Author

Lokesh — Aspiring SOC Analyst