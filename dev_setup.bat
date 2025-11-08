@echo off
REM Development setup script for numgraph (Windows)

echo ==================================
echo numgraph Development Setup
echo ==================================
echo.

REM Check Python version
echo Checking Python version...
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install in development mode
echo.
echo Installing numgraph in development mode...
pip install -e ".[dev]"

REM Run tests to verify installation
echo.
echo Running tests to verify installation...
pytest tests\ -v

echo.
echo ==================================
echo Setup complete!
echo ==================================
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate
echo.
echo Try the quickstart:
echo   python quickstart.py
echo.
echo Run examples:
echo   python examples\circle_equation.py
echo.

pause
