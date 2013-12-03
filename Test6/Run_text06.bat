@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test06.py
echo [Execute]: Monkeyrunner Test06.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test06.py
echo.
echo [Stop]