@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\TakeSnapshot.py
echo [Execute]: Monkeyrunner TakeSnapshot.py
echo.
echo [Start...]
Monkeyrunner %cd%\TakeSnapshot.py
echo.
echo [Stop]