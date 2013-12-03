@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test6.py
echo [Execute]: Monkeyrunner Test6.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test6.py
echo.
echo [Stop]