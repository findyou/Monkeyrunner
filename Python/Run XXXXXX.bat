@echo off
setlocal enabledelayedexpansion
set file_name = "filepath.py"
echo [Current path]: %cd%\%file_name%
echo [Execute]: python %file_name%
echo.
echo [Start...]
python %cd%\%file_name%
echo.
echo [Stop]
pause