@echo off
echo ==============================================
echo Building PDFFigures2 GUI for Windows
echo ==============================================

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH! Please install Python 3.9+
    pause
    exit /b
)

:: Install dependencies
echo Installing requirements...
pip install -r requirements.txt
pip install pyinstaller

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

:: Build using PyInstaller
echo Building executable...
:: We use --noconsole to hide the terminal window on Windows
:: We include the jar and the icon as bundled data
pyinstaller --noconsole --name="PDFFigures2" --add-data="icon_v3.png;." --add-data="pdffigures2.jar;." --icon="icon_v3.png" gui.py

echo ==============================================
echo Build Complete!
echo The Windows executable can be found in the "dist\PDFFigures2" folder.
echo ==============================================
pause
