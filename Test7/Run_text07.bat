@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test07.py
echo [Execute]: Monkeyrunner Test07.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test07.py
echo.
echo [Stop]