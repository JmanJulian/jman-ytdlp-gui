#for this to work you must have pyinstaller package. INSTALL COMAND: "pip install pyinstaller"
pyinstaller --icon=img/Youtube-dl.ico --onefile --add-data="img/video.png:img" --add-data="img/audio.png:img" --add-data="img/Youtube-dl.ico:img" ytdlp-gui_v0.4.pyw
