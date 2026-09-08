# Dharwad Hubli Tutor

Python test project using pytest and Playwright.

## Setup

Create the virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

For Command Prompt, activate the environment with:

```cmd
.venv\Scripts\activate.bat
```

You can also run pytest without activating the environment:

```cmd
.venv\Scripts\python.exe -m pytest -c test_cases\pytest.ini
```

If PowerShell blocks activation, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Run tests

```powershell
pytest -c test_cases\pytest.ini
```

The test fixture launches Chromium in headed mode, so a browser window is expected when browser tests run.# dharwadhublitutorautomationproject
