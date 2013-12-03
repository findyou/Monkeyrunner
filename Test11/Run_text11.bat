@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test11.py
echo [Execute]: Monkeyrunner Test11.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test11.py
echo.
echo [Stop]