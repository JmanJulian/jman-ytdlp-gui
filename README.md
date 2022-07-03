# ytdlp-gui
Simple CrossPlatform GUI for yt-dlp written in Python3.x using PySimpleGUI(TK port) as graphics toolkit.
Since Python and yt-dpl are available for Windows, Linux and Mac it should work on all platforms.
I have tested on Windows and Linux but dont have craple devices to test on.

You can run the precompiled binary(Windows, Linux or Linux ARM32) that has all dependancy built in.
Or in order to run the python file directly you must have Python3 installed (tested on 3.9) also the following lybrarys:
1) PySimpleGUI -> can be installed with command "pip install pysiplegui" in command prompt(windows)/terminal(linux)
2) python-tk or python3-tk (should come preinstalled with python but if not) "sudo apt install python-tk" or "sudo apt install python3-tk" (for debian based linux distros like Ubuntu, Popos, Mint and so on.)
3) ffmpeg has to be installed in order to use the audio/video format options. You can get it from: https://github.com/yt-dlp/FFmpeg-Builds
4) yt-dlp The most important part itself get from: https://github.com/yt-dlp/yt-dlp#release-files. Or press Download yt-dlp from the settings tab wich will get the needed binary based on youre OS (the url that it uses do download them are in the ini file(ini is created on first run)).

Run in command prompt/terminal with command "python ytdlp-gui.pyw" or "python3 ytdlp-gui.pyw"
Or download the precompiled binary (made with pyinstaller)  
  for Windows: BG and EN: [ytdlp-gui_win64.zip](https://github.com/JmanJulian/ytdlp-gui/files/9033382/ytdlp-gui_win64.zip)
  for Linux: BG and EN: [ytdlp-gui-lin64.zip](https://github.com/JmanJulian/ytdlp-gui/files/9033468/ytdlp-gui-lin64.zip)
  for Linux_ARM32: BG and EN: [ytdlp-gui-lin_arm32.zip](https://github.com/JmanJulian/ytdlp-gui/files/9033445/ytdlp-gui-arm32.zip)
  for MacOS: BG and EN: [ytdlp-gui-macOS12.4.zip](https://github.com/JmanJulian/ytdlp-gui/files/9033374/ytdlp-gui-macOS12.4.zip)

![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/W10-4.PNG)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/w7-4.PNG)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/ubuntu_mate_22.04-1.PNG)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/rpi4-12.png)
