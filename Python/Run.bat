@echo off
setlocal enabledelayedexpansion
echo [Current path]: %cd%\filepath.py
echo [Execute]: python filepath.py
echo.
echo [Start...]
python %cd%\filepath.py
echo.
echo [Stop]
pause