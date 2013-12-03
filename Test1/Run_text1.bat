@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test1.py
echo [Execute]: Monkeyrunner Test1.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test1.py
echo.
echo [Stop]