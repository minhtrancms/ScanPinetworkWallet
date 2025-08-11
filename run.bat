@echo off
chcp 65001 > nul
echo Checking Python...

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first and try again.
    pause
    exit /b
)

echo Checking pip...

:: Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing now...
    python -m ensurepip
    python -m pip install --upgrade pip
) else (
    echo Pip is already installed.
)

echo Checking Python libraries...

python -m pip show mnemonic >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing mnemonic library...
    python -m pip install mnemonic
)

python -m pip show web3 >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing web3 library...
    python -m pip install web3
)

python -m pip show eth-account >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing eth-account library...
    python -m pip install eth-account
)

echo All checks completed. Running the program...
python check.py
pause
