@echo off
bash ip.sh
bash ip.sh > ip.txt
python HTTP.py
TIMEOUT /T 10
set /p myVar=<ip.txt
python -m http.server 8000 --bind %myVar%
