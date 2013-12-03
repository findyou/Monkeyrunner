@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test7.py
echo [Execute]: Monkeyrunner Test7.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test7.py
echo.
echo [Stop]