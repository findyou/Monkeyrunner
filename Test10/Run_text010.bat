@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test010.py
echo [Execute]: Monkeyrunner Test010.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test010.py
echo.
echo [Stop]