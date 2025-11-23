# 🧪 Selenium Automation – Notes App Project

**Author:** Ahtasham Shahid — Software QA Engineer  
**Tech Stack:** Python, Selenium, Pytest, WebDriver Manager, GitHub Actions

## 🎯 Automation Project Overview

This project automates UI test scenarios of the **Notes App**, demonstrating professional test automation skills and best practices in framework design.

## 🌟 Notes App (Tested Application)

Welcome to **Notes App** – a better way to track your tasks and stay organized!

### Overview

Stay productive and organized with our easy-to-use notes app.  
Create, edit, categorize, filter, search, and toggle your notes effortlessly. Update your profile and reset your password anytime.  

Simplify your life and never forget a task again!

### Features

These are the core features of the **Notes App** that the automated tests cover:

- **User Authentication**: Create an account and securely log in.
- **Create Notes**: Add new notes with title and description.
- **Edit & Delete Notes**: Update or remove notes anytime.
- **Categorize Notes**: Organize notes into categories.
- **Filter & Search**: Quickly find notes with filters and search functionality.
- **Toggle Notes**: Mark notes as important or completed.
- **Profile Management**: Update your profile information.
- **Password Reset**: Easily reset your password if forgotten.

## 🔥 Automation Project Highlights

- **Page Object Model (POM)**
- **Modular Test Structure**
- Fixtures and utilities for reusable setup
- Comprehensive test coverage
- Validation of:
  - Navigation
  - Form interactions
  - Alerts and prompts
  - Tables
  - Dynamic elements
  - JavaScript functionality
- Screenshots captured on failure
- Rich HTML test reports
- **GitHub Actions CI pipeline**:
  - Auto-run tests on commits and PRs
  - Upload reports and screenshots

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

⚙ Continuous Integration (CI)

This project includes a GitHub Actions pipeline (ci.yml) that:

Installs dependencies

Runs tests on:

Every push

Every Pull Request

Uploads:

HTML report

Failed test screenshots

CI status is visible in repository badges and the workflow tab.

🌐 Target Website

https://practice.expandtesting.com/notes/app/

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

Selenium Automation Portfolio Project (Notes App)
Demonstrates POM framework, automation coverage, reporting, and CI pipeline.