@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test5.py
echo [Execute]: Monkeyrunner Test5.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test5.py
echo.
echo [Stop]