🧪 Selenium Automation – TechBeamers Practice Project

Author: Ahtasham Shahid — Software QA Engineer
Tech Stack: Python, Selenium, Pytest, WebDriver Manager, GitHub Actions

🎯 Project Overview

This project automates UI test scenarios from the TechBeamers Selenium Practice Website, demonstrating professional test automation skills suitable for portfolio and resume.

🔥 What this project highlights

Page Object Model (POM)

Modular test structure

Fixtures and utilities for reusable setup

Comprehensive test coverage

Validation of:

Navigation

Form interaction

Alerts and prompts

Tables

Dynamic elements

JavaScript functionality

Screenshots captured on failure

Rich HTML test reports

GitHub Actions CI pipeline

Tests auto-run on commits and PRs

Test reports and screenshots uploaded as artifacts

📁 Project Structure
.
├── tests/
│   ├── pages/
│   │   └── *.py     # Page Object Model files
│   ├── test_*.py    # Test cases
│   └── utils/       # Helpers, config, common logic
├── reports/         # HTML reports
├── screenshots/     # Screenshots on failure
├── .github/
│   └── workflows/
│       └── ci.yml   # GitHub Actions CI
├── requirements.txt
└── README.md

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/<username>/<repo>.git
cd <repo>

2️⃣ Create a virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate   # Mac / Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Run the tests
pytest

4️⃣ Run tests with HTML report
pytest --html=reports/report.html


HTML report will be generated in:

/reports/report.html

5️⃣ Screenshots on Failure

When a test fails, a screenshot automatically saves in:

/screenshots/

⚙ Continuous Integration (CI)

This project includes a GitHub Actions pipeline (ci.yml) that:

Installs dependencies

Runs tests on:

Every push

Every PR

Uploads:

HTML report

Failed test screenshots

CI status is visible in the repository badges and workflow tab.

🌐 Target Website

Tests use the practice website provided by:

https://techbeamers.com/selenium-webdriver-sample-automation-test/

🧩 Skills Demonstrated

✔ Selenium WebDriver
✔ Page Object Model
✔ Pytest advanced usage
✔ Locators strategies
✔ Waits (explicit / fluent)
✔ Test reporting
✔ CI automation
✔ Git & GitHub workflows
✔ Clean, production-ready test code

📄 Used in Resume

This project is fully designed so it can be referenced as:

Selenium Automation Portfolio Project (TechBeamers Practice Site)
Demonstrates POM framework, automation coverage, reporting, and CI pipeline.