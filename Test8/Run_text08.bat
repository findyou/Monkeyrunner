@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test08.py
echo [Execute]: Monkeyrunner Test08.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test08.py
echo.
echo [Stop]