@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test4.py
echo [Execute]: Monkeyrunner Test4.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test4.py
echo.
echo [Stop]