@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test03.py
echo [Execute]: Monkeyrunner Test03.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test03.py
echo.
echo [Stop]