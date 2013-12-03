@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test05.py
echo [Execute]: Monkeyrunner Test05.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test05.py
echo.
echo [Stop]