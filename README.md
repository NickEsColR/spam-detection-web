# spam-detection-web

## Overview

This is a web platform designed to detect spam messages using state-of-the-art machine learning models. The project is part of the MSc Applied Artificial Intelligence course at ICESI University. It leverages the Hugging Face Transformers library to provide powerful natural language processing capabilities for spam detection.

## Collaborators

- [Nicolas Colmenares](https://github.com/NickEsColR)
- Diego Agudelo
- Carlos Velez
- Jean Pierre Londoño
- Mario J

## Requirements

- **Python Version**: 3.12 or higher
- **Package Manager**: We use `uv` for fast and reliable dependency management

## Libraries Used

This project uses the following main libraries:

- **transformers** (>=4.57.1): State-of-the-art machine learning models from Hugging Face

For a complete list of dependencies, see `pyproject.toml` or `requirements.txt`.

## Installation and Setup

### Option 1: Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver that makes dependency management simple and efficient.

#### Install uv

**Linux/macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or install via pip:

```bash
pip install uv
```

#### Main uv Commands

1. **Initialize a new project:**

   ```bash
   uv init --python 3.12 --name spam-detection-web
   ```

2. **Add a dependency:**

   ```bash
   uv add transformers
   ```

3. **Install production dependencies only:**

   ```bash
   uv sync --no-dev
   ```

4. **Install all dependencies (including development):**

   ```bash
   uv sync
   ```

5. **Add development dependencies:**

   ```bash
   uv add --dev pytest pytest-cov
   ```

6. **Run a Python script:**

   ```bash
   uv run main.py
   ```

7. **Run a command in the virtual environment:**

   ```bash
   uv run python script.py
   ```

8. **Update dependencies:**

   ```bash
   uv lock --upgrade
   ```

9. **Remove a dependency:**

   ```bash
   uv remove <package-name>
   ```

### Option 2: Using Traditional Virtual Environment

#### Creating and Activating Virtual Environment

**Linux/macOS:**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Windows:**

```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install production dependencies only
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest pytest-cov
```

#### Deactivating Virtual Environment

On both Linux/macOS and Windows:

```bash
deactivate
```

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/NickEsColR/spam-detection-web.git
   cd spam-detection-web
   ```

2. Set up your environment using one of the methods above (uv or traditional virtual environment)

3. Start developing!

## Running Tests

This project uses `pytest` for testing. Make sure you have installed development dependencies first.

### Run All Tests

**Using uv:**

```bash
uv run pytest
```

**Using traditional virtual environment:**

```bash
# Make sure virtual environment is activated first and pytest is installed
pytest
```

### Run Tests with Coverage

```bash
# Using uv
uv run pytest --cov=app

# Using traditional venv (activated)
pytest --cov=app
```

### Run Specific Test File

```bash
# Using uv
uv run pytest tests/services/test_spam_detector.py

# Using traditional venv (activated)
pytest tests/services/test_spam_detector.py
```

### Run Specific Test Function

```bash
# Using uv
uv run pytest tests/services/test_spam_detector.py::test_function_name

# Using traditional venv (activated)
pytest tests/services/test_spam_detector.py::test_function_name
```

### Run Tests with Verbose Output

```bash
# Using uv
uv run pytest -v

# Using traditional venv (activated)
pytest -v
```

### Run Tests and Generate HTML Coverage Report

```bash
# Using uv
uv run pytest --cov=app --cov-report=html

# Using traditional venv (activated)
pytest --cov=app --cov-report=html

# Then open htmlcov/index.html in your browser
```

## Run app

```bash
uv run streamlit run app/streamlit_app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
