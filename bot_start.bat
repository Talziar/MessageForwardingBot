@echo off
echo Starting process...
set root= %~dp0
cd %root%
python -m message_forwarding_bot
pause
exit