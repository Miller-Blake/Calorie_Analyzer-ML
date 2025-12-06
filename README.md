# Calorie Input Analyzer & ML

A Python CLI tool that analyzes an Excel sheet containing calories, morning weight, and night weight, then outputs meaningful statistics, trends, graphs, and an estimated maintenance calorie range using machine learning regression.

![Tests Workflow Status](https://github.com/Miller-Blake/Calorie_Analyzer-ML/actions/workflow/status/tests.yml?branch=main)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

## Installation
```bash
# Clone the repository
git clone https://github.com/<your-github-username>/is4010-final-calorie-analyzer.git
cd is4010-final-calorie-analyzer

# Create a virtual environment
py -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows (PowerShell)
. ./venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Navigate to the project root
cd is4010-final-calorie-analyzer

# Activate the virtual environment (if not already active)
# On macOS/Linux
source venv/bin/activate
# On Windows (PowerShell)
. ./venv/Scripts/Activate.ps1

# Analyze an Excel file
py calorie_analyzer/main.py analyze sample_data.xlsx

# Get statistics
py calorie_analyzer/main.py stats sample_data.xlsx

# Generate graphs
py calorie_analyzer/main.py graph sample_data.xlsx --output graphs/

# Estimate TDEE (maintenance calories)
py calorie_analyzer/main.py tdee sample_data.xlsx
```

## Features
- Import Excel files containing calorie and weight data.
- Clean and validate raw data.
- Generate core statistics (date range, averages, daily swings, correlations, Chipotle frequency).
- Estimate maintenance calories (TDEE) using machine learning regression (Baseline and Chipotle-adjusted models).
- Output graphs (trend lines, scatter plots, bar charts).
- Command-line interface with clear help text.

## Testing
```bash
# Navigate to the project root
cd is4010-final-calorie-analyzer

# Activate the virtual environment (if not already active)
# On macOS/Linux
source venv/bin/activate
# On Windows (PowerShell)
. ./venv/Scripts/Activate.ps1

# Run unit tests
pytest is4010-final-calorie-analyzer/tests/
```

## AI-Assisted Development
See AGENTS.md.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.