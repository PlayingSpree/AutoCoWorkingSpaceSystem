del "db.sqlite3" /f /q
del "authapp\migrations\0*" /f /q
del "authapp\migrations\__pycache__" /f /q
del "meetingroom\migrations\0*" /f /q
del "meetingroom\migrations\__pycache__" /f /q
del "coworkingspace\migrations\0*" /f /q
del "coworkingspace\migrations\__pycache__" /f /q
del "iot\migrations\0*" /f /q
del "iot\migrations\__pycache__" /f /q
del "payment\migrations\0*" /f /q
del "payment\migrations\__pycache__" /f /q
del "feedback\migrations\0*" /f /q
del "feedback\migrations\__pycache__" /f /q

@echo off
echo.
echo Database deleted. RIP.
pause