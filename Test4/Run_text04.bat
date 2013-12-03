@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test04.py
echo [Execute]: Monkeyrunner Test04.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test04.py
echo.
echo [Stop]