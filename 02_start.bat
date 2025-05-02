@echo off
cd /d "%~dp0"

:: Activating virtual environment
call .\venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Error activating virtual environment.
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