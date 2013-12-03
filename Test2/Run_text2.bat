@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test2.py
echo [Execute]: Monkeyrunner Test2.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test2.py
echo.
echo [Stop]