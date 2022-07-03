@echo off
REM for this to work you must have pyinstaller module installed to get it run in command prompt: "pip install pyinstaller"
pyinstaller.exe --icon=img/Youtube-dl.ico --noconsole --onefile ytdlp-gui.pyw
