@echo off
cd venv\Scripts
echo [Activating virtual venv]
call activate.bat
echo.
echo Done
cd ..
cd ..
echo.
echo [Running Server]
echo.
py main.py
pause