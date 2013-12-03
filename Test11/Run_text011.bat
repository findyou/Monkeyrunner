@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test011.py
echo [Execute]: Monkeyrunner Test011.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test011.py
echo.
echo [Stop]