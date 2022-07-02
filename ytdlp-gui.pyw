#!/usr/bin/env python
from pickle import TRUE
from turtle import window_height
import PySimpleGUI as sg    #INSTALL WITH COMMAND: "pip install pysimplegui"  FOR UBUNTU also: "sudo apt install python3-tk"
import platform
import subprocess
from notifypy import Notify #INSTALL WITH COMMAND: "pip install notify-py"
import os
import sys
import configparser
import urllib.request

version = ' v0.4'
console = True

# Download the file from `url` and save it locally under `file_name`:
def downloadFile(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

#START CONFIG FILE HANDLING
def updateConfigFile():
    with open('ytdlp-gui.ini', 'w') as configfile:								#open config file for writing. if it does not exist it will be created.
        config.write(configfile)												#write the config variable data to config file

config = configparser.ConfigParser()											#define config data varaiable
if not os.path.exists('ytdlp-gui.ini'):											#if config file does not exist
    config['DEFAULT'] = {														#define file contents
        'Language':'bg',
        'theme':'SystemDefault1',
        'ytdlp_url_win':'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_x86.exe',
        'ytdlp_url_lin':'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp',
        'ytdlp_url_mac':'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos',
        }
    updateConfigFile()															#write to config file

config.read('ytdlp-gui.ini')													#read config file
setLocal = config.get('DEFAULT','Language')										#get language from config file language key
setTheme = config.get('DEFAULT','theme')										#get theme from config file theme key
ytdlp_url_win = config.get('DEFAULT','ytdlp_url_win')
ytdlp_url_lin = config.get('DEFAULT','ytdlp_url_lin')
ytdlp_url_mac = config.get('DEFAULT','ytdlp_url_mac')
#END CONFIG FILE HANDLING

if not os.path.exists('Downloads'):												#If folder Downloads in current directory does not exist
    os.makedirs('Downloads')													#Create Downloads directory

locale = {
    "bg": {
        'complete'     : "Завърши!",
        'download_of'  : "Изтеглянето на:\n",
        'dcomplete_msg': "Завърши!\n Изтеглянето на:\n",
        'MaxRez'       : "Макс. резолюция",
        'about'        : "Елементарен графичен интерфейс за командната програма yt-dlp. Писана на Python3, PySimpleGUI(tk) и notify-py ",
        'about2'       : "Автор: Илиян Пиргозлиев / 2022",
        'url'          : "сложи URL тук ->",
        'video'        : "Видео",
        'audio'        : "Аудио",
        'settings'     : "Настройки(Settings)",
        'abouttab'     : "За програмата",
        'open_dldir'   : "Отвори папка с изтеглени",
        'download'     : "Изтегли",
        'apply'        : "Приложи",
        'downytdlpbin' : "Изтегли yt-dlp",
        'nourl'        : "Трябва да зададете URL!",
        'emb_sub'      : "само за видео формати mp4,webm,mkv",
        #'emb_thmb'    : "само за аудио формати",
        'console'      : "данните от yt-dlp ще се изпишат тук:",
    },
    "en": {
        'complete'     : "Complete!",
        'download_of'  : "Download of:\n",
        'dcomplete_msg': "Complete!\n Download of:\n",
        'MaxRez'       : "Max. resolution",
        'about'        : "Simple graphical interface for yt-dlp. Writen in Python3, PySimpleGUI(tk) and notify-py ",
        'about2'       : "Author: Iliyan Pirgozliev / 2022",
        'url'          : "put URL here ->",
        'video'        : "Video",
        'audio'        : "Audio",
        'settings'     : "Settings",
        'abouttab'     : "About",
        'open_dldir'   : "Open downloads folder",
        'download'     : "Download",
        'apply'        : "Apply",
        'downytdlpbin' : "Download yt-dlp",
        'nourl'        : "You must enter a URL!",
        'emb_sub'      : "only for video format mp4,webm,mkv",
        #'emb_thmb'    : "only for audio formats",
        'console'      : "yt-dlp console output will be printed here:",
    }
}

if getattr(sys, 'frozen', False):
    audio_img = os.path.join(sys._MEIPASS, 'img/audio.png')
    video_img = os.path.join(sys._MEIPASS, 'img/video.png')
    icon_img  = os.path.join(sys._MEIPASS, 'img/Youtube-dl.ico')
else:
    audio_img = './img/audio.png'
    video_img = './img/video.png'
    icon_img  = './img/Youtube-dl.ico'

def notification(url):
    notification = Notify()
    notification.title   = locale[setLocal]['complete']
    notification.message = locale[setLocal]['download_of'] + url
    notification.icon = icon_img
    notification.send()

def ShellOpen(path='Downloads'):
	subprocess.run([ shell_open, path ])

def run_cmd(cmd):
    proc=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line.decode("utf-8") )
        print(line, flush=True)
    proc.wait()

allthemes = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
sg.theme(setTheme)
ttk_theme='default'

if platform.system() == "Windows":
    if int(platform.win32_ver()[0]) < 8:
        def notification(url):
            subprocess.run(['msg', '*', '/time:3', locale[setLocal]['dcomplete_msg'] + url])
    if setTheme == 'SystemDefault1': ttk_theme='vista'
    FONTS='Tahoma 10'
    slash='\\'
    shell_open='start'
    ytdlp_url = ytdlp_url_win
    def ShellOpen(path='Downloads'):
        subprocess.run([ shell_open, path ], shell=True)

elif platform.system() == "Linux":
    if setTheme == 'SystemDefault1': ttk_theme='clam'
    FONTS='Ubuntu 9'
    slash='/'
    shell_open='xdg-open'
    ytdlp_url = ytdlp_url_lin

elif platform.system() == 'Darwin':
    if setTheme == 'SystemDefault1': ttk_theme='clam'
    FONTS='arial 9'
    slash='/'
    shell_open='open'
    ytdlp_url = ytdlp_url_mac

def rungui():
    VideoTablayout = [[
        sg.Column([
            [sg.Image(video_img, size=(120,100))]
            ]),
        sg.Column([
            [sg.Radio('Auto', "RADIO1", key='-AUTV-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('Webm', "RADIO1", key='-WEBM-', size=(6,1)), sg.Text(locale[setLocal]['MaxRez'], expand_x=True)],
            [sg.Radio('Mp4 ', "RADIO1", key='-MP4-', size=(6,1)), sg.Radio('Mkv ', "RADIO1", key='-MKV-', size=(6,1)), sg.Combo(['Auto','144','240','360','480','720','1080','1440','2160'], default_value='Auto', key=('-REZ-'), expand_x=True)],
            [sg.Radio('Flv ', "RADIO1", key='-FLV-', size=(6,1)), sg.Radio('Avi ', "RADIO1", key='-AVI-', size=(6,1)), sg.Checkbox('Embed Sub', key='-EMBSUB-', tooltip=locale[setLocal]['emb_sub'])],
            [sg.Radio('Ogg ', "RADIO1", key='-OGG-', size=(6,1))]
            ], expand_x=True)
        ]]
    AudioTablayout = [[
        sg.Column([
            [sg.Image(audio_img, size=(120,100))]
            ]),
        sg.Column([
            [sg.Radio('Auto', "RADIO2", key='-AUTA-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('m4a ', "RADIO2", key='-M4A-', size=(4,1)), sg.Checkbox('Embed Thumb', default=True, key='-EMBTHMB-', pad=((6,0),(0,0)))],
            [sg.Radio('Mp3 ', "RADIO2", key='-MP3-', size=(6,1)), sg.Radio('opus', "RADIO2", key='-OPUS-', size=(4,1))],
            [sg.Radio('AAC ', "RADIO2", key='-AAC-', size=(6,1)), sg.Radio('wav ', "RADIO2", key='-WAV-', size=(4,1))],
            [sg.Radio('Flac', "RADIO2", key='-FLAC-', size=(6,1))]
            ])
        ]]
    ConfigTablayout = [
        [sg.Text('Language:', pad=((10,0),(5,0))), sg.Combo(['bg','en'], default_value=setLocal, key='-LANG-', pad=((0,0),(6,0))), sg.Text('Theme:',pad=((10,0),(5,0))), sg.Combo(allthemes, default_value=setTheme, key='-THEME-', pad=((0,0),(5,0))) ],
        [sg.Button(locale[setLocal]['downytdlpbin'],key='-GET1-', pad=((10,0),(40,5)), size=(20,1)), sg.Push(), sg.Button(locale[setLocal]['apply'], key='-APPLY-', pad=((0,10),(40,5)), size=(8,1))]
        ]
    AboutTablayout = [
        [sg.Text(locale[setLocal]['about'], pad=((10,0),(5,0)), size=(50,0) )],
        [sg.Button('Project Home:',key='-GOHOME-', pad=((10,0),(0,0))), sg.Input('https://github.com/JmanJulian/ytdlp-gui', key='-HOMEPAGE-', pad=((0,3),(0,0)))],
        [sg.Text(locale[setLocal]['about2'], pad=((10,0),(0,0)) )]
        ]

    MainWinlayout = [
        [sg.Text(locale[setLocal]['url'], pad=((4,0),(3,0))), sg.Input("", key='-URL-', right_click_menu=[[''], ['Paste']], size=(100,20), pad=((0,4),(5,0)) )],
        [sg.TabGroup([
            [ sg.Tab(locale[setLocal]['video'],    VideoTablayout, key='-VIDEO-') ],
            [ sg.Tab(locale[setLocal]['audio'],    AudioTablayout, key='-AUDIO-') ],
            [ sg.Tab(locale[setLocal]['settings'], ConfigTablayout, key='-CONF-') ],
            [ sg.Tab(locale[setLocal]['abouttab'], AboutTablayout, key='-ABOUT-') ]
            ], key=('-TAB-'), expand_x=True)],
        [sg.Button(locale[setLocal]['open_dldir'], key='-ODL-', expand_x=True), sg.B('⥯',key='-UPDOWN-'), sg.Button(locale[setLocal]['download'], key='-DL-', expand_x=True)],
        [sg.Multiline(size=(360,6),background_color='black', text_color='green',reroute_stdout=TRUE,reroute_cprint=TRUE,reroute_stderr=TRUE,autoscroll=TRUE, auto_refresh=True, key='-CONSOLE-')]
        ]

    window = sg.Window("Ytdlp-GUI"+version,MainWinlayout, size=(380,280),
        ttk_theme=ttk_theme, use_ttk_buttons=True,
        element_padding=(0,0),
        margins=(0,0),
        font=FONTS,
        resizable=False,
        finalize=True
    )
    return window

window = rungui()
print(locale[setLocal]['console'])

while True:
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event=="Exit":
        break
        window.close()
        exit
    if event == 'Paste':
        window['-URL-'].update(sg.clipboard_get())
    if event == '-ODL-':
        ShellOpen()
    if event == '-DL-':
        if values['-URL-'] == "":
            sg.popup(locale[setLocal]['nourl'])
            continue

        if values['-TAB-'] == '-VIDEO-':
            vformat=''
            convert_to='--recode-video='
            resolution = ''
            recode_to = ''
            if values['-MP4-']: vformat='mp4'
            if values['-FLV-']: vformat='flv'
            if values['-OGG-']: vformat='ogg'
            if values['-WEBM-']:vformat='webm'
            if values['-MKV-']: vformat='mkv'
            if values['-AVI-']: vformat='avi'
            if not values['-AUTV-']: recode_to= "--recode-video=" + vformat
            if values['-REZ-'] != 'Auto':
                resolution = "-f bestvideo[height<=" + values['-REZ-'] + "]+bestaudio"
            embed_sub = '--no-embed-subs'
            if values['-EMBSUB-']: embed_sub = '--embed-subs'
            run_cmd(['./yt-dlp', values['-URL-'], resolution, embed_sub, recode_to, '--output=Downloads'+slash+'%(uploader)s%(title)s.%(ext)s'])
            notification(values['-URL-'])
        if values['-TAB-'] == '-AUDIO-':
            aformat='best'
            convert_to='--audio-format='
            if values['-MP3-']: aformat='mp3'
            if values['-AAC-']: aformat='aac'
            if values['-FLAC-']:aformat='flac'
            if values['-M4A-']: aformat='m4a'
            if values['-OPUS-']:aformat='opus'
            if values['-WAV-']: aformat='wav'
            embed_thumb = '--no-embed-thumbnail'
            if values['-EMBTHMB-']: embed_thumb = '--embed-thumbnail'
            run_cmd(['./yt-dlp', values['-URL-'], '-x', convert_to+aformat, embed_thumb,'--output=Downloads'+slash+'%(uploader)s%(title)s.%(ext)s'])
            notification(values['-URL-'])
    if event == '-APPLY-':
        if setLocal != values['-LANG-']:
            setLocal = values['-LANG-']
            config.set('DEFAULT','Language', setLocal)
            updateConfigFile()
            window.close()
            window = rungui()
        if values['-THEME-'] != setTheme:
            setTheme = values['-THEME-']
            sg.theme(setTheme)
            config.set('DEFAULT','theme', setTheme)
            updateConfigFile()
            ttk_theme='default'
            window.close()
            window = rungui()
            print('Theme change to:' + sg.theme())
    if event == '-GET1-':
        downloadFile(ytdlp_url, 'yt-dlp')
        os.chmod("./yt-dlp", 0o775)
        notification(ytdlp_url)
    if event == '-GOHOME-':
        ShellOpen(values['-HOMEPAGE-'])
    if event == '-UPDOWN-':
        if console:
            window['-CONSOLE-'].update(visible=False)
            console = False
            window.Size=(380,183)
        else:
            window['-CONSOLE-'].update(visible=True)
            console = True
            window.Size=(380,280)
