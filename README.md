# ytdlp-gui
Simple CrossPlatform GUI for yt-dlp written in Python3.x using PySimpleGUI(TK port) as graphics toolkit.
Since Python and yt-dpl are available for Windows, Linux and Mac it should work on all platforms.
I have tested on Windows and Linux but dont have craple devices to test on.

You can run the precompiled binary(Windows, Linux or Linux ARM32) that has all dependancy built in.
Or in order to run the python file directly you must have Python3 installed (tested on 3.9) also the following lybrarys:
1) PySimpleGUI -> can be installed with command "pip install pysiplegui" in command prompt(windows)/terminal(linux)
2) notify-py -> can be installed with command "pip install notify-py" in command prompt(windows)/terminal(linux)
3) python-tk or python3-tk (should come preinstalled with python but if not) "sudo apt install python-tk" or "sudo apt install python3-tk" (for debian based linux distros like Ubuntu, Popos, Mint and so on.)
4) ffmpeg has to be installed in order to use the audio/video format options. You can get it from: https://github.com/yt-dlp/FFmpeg-Builds
5) yt-dlp The most important part itself get from: https://github.com/yt-dlp/yt-dlp#release-files

Run in command prompt/terminal with command "python ytdlp-gui.py"
Or download the precompiled binary (made with pyinstaller)  
  for Windows: https://github.com/JmanJulian/ytdlp-gui/files/8888536/ytdlp-gui-en.zip
  for Linux: https://github.com/JmanJulian/ytdlp-gui/files/8886228/ytdlp-gui-linux64.zip
  for Linux_ARM32: https://github.com/JmanJulian/ytdlp-gui/files/8886301/ytdlp-gui-linux-arm32.zip

![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/win10-12.png)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/Win7-12.png)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/ubuntu_mate_22.04-1.PNG)
![alt tag](https://github.com/JmanJulian/ytdlp-gui/blob/main/img/Screenshot/rpi4-12.png)

