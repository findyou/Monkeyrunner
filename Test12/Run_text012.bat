@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test012.py
echo [Execute]: Monkeyrunner Test012.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test012.py
echo.
echo [Stop]