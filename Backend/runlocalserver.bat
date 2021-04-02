@echo off
cd venv\Scripts
echo [Activating virtual venv]
call activate.bat
echo.
echo Done
cd ..
cd ..
echo.
echo [Migating Databases]
echo.
py manage.py makemigrations
py manage.py migrate
echo.
echo [Running Server]
echo.
py manage.py runserver 0.0.0.0:8000
pause