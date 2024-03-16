@echo off
echo Checking Python version...
set root= %~dp0
cd %root%
python --version
pause
exit