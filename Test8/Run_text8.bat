@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test8.py
echo [Execute]: Monkeyrunner Test8.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test8.py
echo.
echo [Stop]