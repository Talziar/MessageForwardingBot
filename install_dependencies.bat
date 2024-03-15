@echo off
echo Starting process...
set root= %~dp0
cd %root%
pip3 install .
pause
exit