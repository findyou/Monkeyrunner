@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test10.py
echo [Execute]: Monkeyrunner Test10.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test10.py
echo.
echo [Stop]