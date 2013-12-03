@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test02.py
echo [Execute]: Monkeyrunner Test02.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test02.py
echo.
echo [Stop]