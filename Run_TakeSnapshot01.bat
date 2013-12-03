@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\TakeSnapshot01.py
echo [Execute]: Monkeyrunner TakeSnapshot01.py
echo.
echo [Start...]
Monkeyrunner %cd%\TakeSnapshot01.py
echo.
echo [Stop]