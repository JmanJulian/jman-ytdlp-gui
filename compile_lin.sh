#for this to work you must have pyinstaller module installed -> "pip install pyinstaller" or "pip3 install pyinstaller"
pyinstaller --icon=img/Youtube-dl.ico --add-data="img/Youtube-dl.ico:img" --onefile ytdlp-gui.pyw
