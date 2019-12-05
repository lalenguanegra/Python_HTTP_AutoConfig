@echo off
bash ip.sh
bash ip.sh > ip.txt
set /p myVar=<ip.txt
TIMEOUT /T 10
python -m http.server 8080 --bind %myVar%
