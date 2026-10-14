# Python API Test Automation Framework

## Overview

A Python-based API test automation framework built with pytest and requests. The project demonstrates reusable API communication, automated response validation, error handling, logging, and test reporting.

## Technologies

* Python
* pytest
* Requests
* JSON Schema
* pytest-html

## Project Structure

```text
API_Test_Automation_Framework/
├── clients/
│   └── api_client.py
├── schemas/
│   └── post_schema.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_api_client.py
│   ├── test_api_crud.py
│   └── test_api_schema.py
├── utils/
│   └── assertions.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Features

* Reusable HTTP client for GET, POST, PUT, and DELETE requests
* Configurable base URL and request timeout
* Logging of HTTP requests, responses, and execution time
* HTTP error handling
* Positive and negative API tests
* Parametrized tests
* JSON Schema validation
* HTML test reporting

## Installation

Clone the repository and navigate to the project directory.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Generate an HTML report:

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

## Configuration

The default API base URL is:

`https://jsonplaceholder.typicode.com`

You can override it using the `API_BASE_URL` environment variable.

PowerShell example:

```powershell
$env:API_BASE_URL = "https://jsonplaceholder.typicode.com"
python -m pytest -v
```

## Test Coverage

The framework includes tests for API response status codes, required JSON fields, resource identifiers, response content, client error handling, and JSON Schema validation.

## Disclaimer

This project uses JSONPlaceholder, a public testing API. It is intended for learning and demonstration purposes.