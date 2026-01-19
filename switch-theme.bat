@echo off
REM Quick Theme Switcher for YASB
REM Usage: switch-theme.bat [theme-name]

cd /d "%~dp0"

if "%1"=="" (
    python switch_theme.py
) else (
    python switch_theme.py %1
)

pause
