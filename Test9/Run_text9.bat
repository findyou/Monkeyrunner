@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test9.py
echo [Execute]: Monkeyrunner Test9.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test9.py
echo.
echo [Stop]