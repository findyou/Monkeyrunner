@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test3.py
echo [Execute]: Monkeyrunner Test3.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test3.py
echo.
echo [Stop]