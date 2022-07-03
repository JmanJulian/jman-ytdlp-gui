@echo off
REM for this to work you must have pyinstaller package. INSTALL COMAND: "pip install pyinstaller"
pyinstaller.exe --icon=img/Youtube-dl.ico --onefile --noconsole ytdlp-gui.pyw
