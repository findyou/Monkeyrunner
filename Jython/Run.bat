@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\filepath.py
echo [Execute]: monkeyrunner filepath.py
echo.
echo [Start...]
monkeyrunner %cd%\filepath.py
echo.
echo [Stop]
pause