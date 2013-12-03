@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\Test12.py
echo [Execute]: Monkeyrunner Test12.py
echo.
echo [Start...]
Monkeyrunner %cd%\Test12.py
echo.
echo [Stop]