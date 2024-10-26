### Rule-Engine
Developed a simple 3-tier rule engine application (Simple UI, API, and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend, etc. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

### Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)

## Overview

This application:
1. Allows users to create rules using a simple string format.
2. Combines multiple rules into a single rule.
3. Evaluates rules against provided data.
4. Stores rules in an SQLite database.

## Features

- **Rule Creation:** Create rules using a simple string format and store them in the database.
- **Rule Combination:** Combine multiple rules into a single rule.
- **Rule Evaluation:** Evaluate rules against provided data and get the result.
- **Web Interface:** Simple and intuitive web interface for creating, combining, and evaluating rules.

## Requirements

To run this application, ensure the following dependencies are installed:
- `python3`
- `SQLAlchemy`
- `pytest`
- `Flask`

You can install the Python packages using the following:
```bash
pip install Flask SQLAlchemy pytest
```

## Setup

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```
# Initialise the Database
Run the following commands to set up the database:
```bash
from your_project import create_app, db
    app = create_app()
    with app.app_context():
    db.create_all()
```

## Configuration
The application uses a SQLite database by default. You can configure the database URI in the create_app function in __init__.py:
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
```

## Usage

# Run the Application
```bash
flask run
```
# Access the Web Interface
Open your browser and navigate to http://localhost:5000 to access the web interface.

# Interact with the Application
- **Create Rule:** Navigate to the "Create Rule" page, enter a rule string, and submit the form to create a rule.
- **Combine Rules:** Navigate to the "Combine Rules" page, enter rule IDs, and submit the form to combine rules.
- **Evaluate Rule:** Navigate to the "Evaluate Rule" page, enter the AST JSON and data JSON, and submit the form to evaluate the rule.

# Demo
