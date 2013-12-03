@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test01.py
echo [Execute]: Monkeyrunner Test01.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test01.py
echo.
echo [Stop]