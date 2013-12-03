@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test09.py
echo [Execute]: Monkeyrunner Test09.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test09.py
echo.
echo [Stop]