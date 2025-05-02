@echo off
cd /d "%~dp0"

:: Allow to execute .bat scripts
powershell -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"

:: Creating venv for specific Python version
if not exist "venv\" (
    echo Creating venv with Python 3.13
    py -3.13 -m venv venv
    if %ERRORLEVEL% NEQ 0 (
        echo Error creating virtual environment.
        exit /b %ERRORLEVEL%
    )
)

:: Activating virtual environment
call .\venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Error activating virtual environment.
    exit /b %ERRORLEVEL%
)

:: Upgrading pip
python -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo Error upgrading pip.
    exit /b %ERRORLEVEL%
)

:: Installing dependencies
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error installing dependencies.
    exit /b %ERRORLEVEL%
)

:: Running the application
python app.py
if %ERRORLEVEL% NEQ 0 (
    echo Error running the application.
    exit /b %ERRORLEVEL%
)

:: Holding Console for logs
echo.
echo Script is stopped, waiting for exit
pause >nul