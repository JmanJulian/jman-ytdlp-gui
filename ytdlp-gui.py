#!/usr/bin/env python
import PySimpleGUI as sg    #INSTALL WITH COMMAND: "pip install pysimplegui"  FOR UBUNTU also: "sudo apt install python3-tk"
import platform
import subprocess
from notifypy import Notify #INSTALL WITH COMMAND: "pip install notify-py"
import os
import sys

if not os.path.exists('Downloads'):
    os.makedirs('Downloads')

setLocal = "bg"
locale = {
    "bg": {
        'complete'     : "Завърши!",
        'download_of'  : "Download of:\n",
        'dcomplete_msg': "Завърши!\n Изтеглянето на:\n",
        'MaxRez'       : "Макс. резолюция",
        'about'        : "Елементарен графичен интерфейс за командната програма yt-dlp. Писана на Python3, PySimpleGUI(tk) и notify-py ",
        'about2'       : "Автор: Илиян Пиргозлиев / 2022",
        'url'          : "сложи URL тук ->",
        'video'        : "Видео",
        'audio'        : "Аудио",
        'settings'     : "Настройки",
        'abouttab'     : "За програмата",
        'open_dldir'   : "Отвори папка с изтеглени",
        'download'     : "Изтегли"
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
        'download'     : "Download"
    }
}
#locale[setLocal]['open_dldir']

if getattr(sys, 'frozen', False):
    audio_img = os.path.join(sys._MEIPASS, 'img/audio.png')
    video_img = os.path.join(sys._MEIPASS, 'img/video.png')
    icon_img  = os.path.join(sys._MEIPASS, 'img/Youtube-dl.ico')
else:
    audio_img = 'img/audio.png'
    video_img = 'img/video.png'
    icon_img  = 'img/Youtube-dl.ico'

def notification(url):
    notification = Notify()
    notification.title   = locale[setLocal]['complete']
    notification.message = locale[setLocal]['download_of'] + url
    notification.icon = icon_img
    notification.send()
allthemes = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
sg.theme('SystemDefault1') #sg.theme('Default1')
if platform.system() == "Windows":
    if int(platform.win32_ver()[0]) < 8:
        def notification(url):
            subprocess.run(['msg', '*', '/time:3', locale[setLocal]['dcomplete_msg'] + url])
    ttk_theme='vista'
    FONTS='Tahoma 10'
    slash='\\'
    def openFolder(path='Downloads'):
        subprocess.Popen(['explorer', path])
elif platform.system() == "Linux":
    ttk_theme='clam'
    FONTS='Ubuntu 9'
    slash='/'
    def openFolder(path='Downloads'):
        subprocess.Popen(['xdg-open', path])
elif platform.system() == 'Darwin':
    ttk_theme='Clam'
    FONTS='San Francisco 9'
    slash='/'
    def openFolder(path='Downloads'):
        subprocess.check_call(['open', '--', path])
def rungui():
    VideoTablayout = [[
        sg.Column([
            [sg.Image(video_img, size=(120,100))]
            ]),
        sg.Column([
            [sg.Radio('Auto', "RADIO1", key='-AUTV-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('Webm', "RADIO1", key='-WEBM-', default=False, size=(6,1)), sg.Text(locale[setLocal]['MaxRez'], expand_x=True)],
            [sg.Radio('Mp4 ', "RADIO1", key='-MP4-',  default=False, size=(6,1)), sg.Radio('Mkv ', "RADIO1", key='-MKV-',  default=False, size=(6,1)), sg.Combo(['Auto','144','240','360','480','720','1080','1440','2160'], default_value='Auto', key=('-REZ-'), expand_x=True)],
            [sg.Radio('Flv ', "RADIO1", key='-FLV-',  default=False, size=(6,1)), sg.Radio('Avi ', "RADIO1", key='-AVI-',  default=False, size=(6,1))],
            [sg.Radio('Ogg ', "RADIO1", key='-OGG-',  default=False, size=(6,1))]
            ], expand_x=True)
        ]]
    AudioTablayout = [[
        sg.Column([
            [sg.Image(audio_img, size=(120,100))]
            ]),
        sg.Column([
            [sg.Radio('Auto', "RADIO2", key='-AUTA-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('m4a ', "RADIO2", key='-M4A-',  default=False, size=(6,1))],
            [sg.Radio('Mp3 ', "RADIO2", key='-MP3-',  default=False, size=(6,1)), sg.Radio('opus', "RADIO2", key='-OPUS-', default=False, size=(6,1))],
            [sg.Radio('AAC ', "RADIO2", key='-AAC-',  default=False, size=(6,1)), sg.Radio('wav ', "RADIO2", key='-WAV-',  default=False, size=(6,1))],
            [sg.Radio('Flac', "RADIO2", key='-FLAC-', default=False, size=(6,1))]
            ])
        ]]
    ConfigTablayout = [
        [sg.Text('Language:', pad=((10,0),(5,0))), sg.Combo(['bg','en'], default_value='bg', key='-LANG-', pad=((0,0),(6,0))), sg.Text('Theme:',pad=((10,0),(5,0))), sg.Combo(allthemes, default_value='SystemDefault1', key='-THEME-', pad=((0,0),(5,0))) ],
        [sg.Push(), sg.Button('Apply', key='-APPLY-', pad=((0,10),(40,5)), size=(8,1))]
        ]
    AboutTablayout = [
        [sg.Text(locale[setLocal]['about'], pad=((10,0),(5,0)), size=(50, 4) )],
        [sg.Text(locale[setLocal]['about2'], pad=((10,10),(0,0)) )]
        ]


    MainWinlayout = [
        [sg.Text(locale[setLocal]['url'], pad=((4,0),(3,0))), sg.Input("", key='-URL-', right_click_menu=[[''], ['Paste']], size=(100,20), pad=((0,4),(5,0)) )],
        [sg.TabGroup([
            [ sg.Tab(locale[setLocal]['video'],    VideoTablayout, key='-VIDEO-') ],
            [ sg.Tab(locale[setLocal]['audio'],    AudioTablayout, key='-AUDIO-') ],
            [ sg.Tab(locale[setLocal]['settings'], ConfigTablayout, key='-CONF-') ],
            [ sg.Tab(locale[setLocal]['abouttab'], AboutTablayout, key='-ABOUT-') ]
            ], key=('-TAB-'), expand_x=True)],
        [sg.Button(locale[setLocal]['open_dldir'], key='-ODL-', expand_x=True, expand_y=True), sg.Button(locale[setLocal]['download'], key='-DL-', expand_x=True, expand_y=True)]
        ]


    window = sg.Window("Ytdlp-GUI",MainWinlayout, size=(380,200),
        ttk_theme=ttk_theme, use_ttk_buttons=True,
        element_padding=(0,0),
        margins=(0,0),
        font=FONTS,
        resizable=False,
        finalize=True
    )
    return window

window = rungui()

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event=="Exit":
        break
        window.close()
        exit
    if event == 'Paste':
        window['-URL-'].update(sg.clipboard_get())
    if event == '-ODL-':
        openFolder()
    if event == '-DL-':
        print(values['-MP3-'])
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
            result=subprocess.run(['yt-dlp', values['-URL-'], resolution, recode_to, '--output=Downloads'+slash+'%(uploader)s%(title)s.%(ext)s']) #, capture_output=True
            #print(result)
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
            subprocess.run(['yt-dlp', values['-URL-'], '-x', convert_to+aformat, '--output=Downloads'+slash+'%(uploader)s%(title)s.%(ext)s']) #, capture_output=True
            notification(values['-URL-'])
    if event == '-APPLY-':
        if setLocal != values['-LANG-']:
            setLocal = values['-LANG-']
            window.close()
            window = rungui()
        if values['-THEME-'] != 'SystemDefault1':
            sg.theme(values['-THEME-'])
            ttk_theme='default'
            window.close()
            window = rungui()