# spam-detection-web

## Overview

This is a web platform designed to detect spam messages using state-of-the-art machine learning models. The project is part of the MSc Applied Artificial Intelligence course at ICESI University. It leverages the Hugging Face Transformers library to provide powerful natural language processing capabilities for spam detection.

## Participants and Collaborators

- **Course**: MSc Applied Artificial Intelligence
- **Institution**: ICESI University
- **Contributors**: Course participants and instructors

If you'd like to contribute to this project, please feel free to open an issue or submit a pull request.

## Requirements

- **Python Version**: 3.12 or higher
- **Package Manager**: We use `uv` for fast and reliable dependency management

## Libraries Used

This project uses the following main libraries:

- **transformers** (>=4.57.1): State-of-the-art machine learning models from Hugging Face
- **Additional dependencies** are automatically managed by `uv` and include:
  - numpy
  - tokenizers
  - huggingface-hub
  - safetensors
  - requests
  - pyyaml
  - and more...

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

3. **Install all dependencies:**
   ```bash
   uv sync
   ```

4. **Run a Python script:**
   ```bash
   uv run main.py
   ```

5. **Run a command in the virtual environment:**
   ```bash
   uv run python script.py
   ```

6. **Update dependencies:**
   ```bash
   uv lock --upgrade
   ```

7. **Remove a dependency:**
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

# Install dependencies
pip install -r requirements.txt
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
