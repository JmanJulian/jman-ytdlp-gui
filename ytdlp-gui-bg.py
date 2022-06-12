#!/usr/bin/env python
import PySimpleGUI as sg #pip install pysimplegui    #pip install python-tk or pip install python3-tk
import platform
import subprocess
from notifypy import Notify #pip install notify-py

def notification(url):
    notification = Notify()
    notification.title   = "Завърши!"
    notification.message = "Изтеглянето на:\n" + url
    notification.send()

sg.theme('SystemDefault1') #sg.theme('Default1')
if platform.system() == "Windows":
    if int(platform.win32_ver()[0]) < 8:
        def notification(url):
            subprocess.run(['msg', '*', '/time:3', "Завърши!\n Изтеглянето на:\n" + url])
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

VideoTablayout = [[
    sg.Column([
        [sg.Image('img/video.png', size=(120,100))]
        ]),
    sg.Column([
        [sg.Radio('Auto', "RADIO1", key='-AUTV-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('Webm', "RADIO1", key='-WEBM-', default=False, size=(6,1)), sg.Text('Макс. резолюция', expand_x=True)],
        [sg.Radio('Mp4 ', "RADIO1", key='-MP4-',  default=False, size=(6,1)), sg.Radio('Mkv ', "RADIO1", key='-MKV-',  default=False, size=(6,1)), sg.Combo(['Auto','144','240','360','480','720','1080','1440','2160'], default_value='Auto', key=('-REZ-'), expand_x=True)],
        [sg.Radio('Flv ', "RADIO1", key='-FLV-',  default=False, size=(6,1)), sg.Radio('Avi ', "RADIO1", key='-AVI-',  default=False, size=(6,1))],
        [sg.Radio('Ogg ', "RADIO1", key='-OGG-',  default=False, size=(6,1))]
        ], expand_x=True)
    ]]
AudioTablayout = [[
    sg.Column([
        [sg.Image('img/audio.png', size=(120,100))]
        ]),
    sg.Column([
        [sg.Radio('Auto', "RADIO2", key='-AUTA-', default=True,  pad=(0,0), size=(6,1)), sg.Radio('m4a ', "RADIO2", key='-M4A-',  default=False, size=(6,1))],
        [sg.Radio('Mp3 ', "RADIO2", key='-MP3-',  default=False, size=(6,1)), sg.Radio('opus', "RADIO2", key='-OPUS-', default=False, size=(6,1))],
        [sg.Radio('AAC ', "RADIO2", key='-AAC-',  default=False, size=(6,1)), sg.Radio('wav ', "RADIO2", key='-WAV-',  default=False, size=(6,1))],
        [sg.Radio('Flac', "RADIO2", key='-FLAC-', default=False, size=(6,1))]
        ])
    ]]
ConfigTablayout = [[
    sg.Text('test')
    ]]
AboutTablayout = [
    [sg.Text('Елементарен графичен интерфейс за командната програма yt-dlp. Писана на Python3, PySimpleGUI(tk) и notify-py ', pad=((10,0),(5,0)), size=(50, 4) )],
    [sg.Text('Автор(Author): Илиян Пиргозлиев (Iliyan Pirgozliev) / 2022', pad=((10,10),(0,0)) )]
    ]


MainWinlayout = [
    [sg.Text("сложи URL тук ->", pad=((4,0),(3,0))), sg.Input("", key='-URL-', right_click_menu=[[''], ['Постави']], size=(100,20), pad=((0,4),(5,0)) )],
    [sg.TabGroup([
        [ sg.Tab('Видео', VideoTablayout, key='-VIDEO-') ],
        [ sg.Tab('Аудио', AudioTablayout, key='-AUDIO-') ],
        [ sg.Tab('Настройки', ConfigTablayout, key='-CONF-') ],
        [ sg.Tab('За програмата', AboutTablayout, key='-ABOUT-') ]
        ], key=('-TAB-'), expand_x=True)],
    [sg.Button("Отвори папка с изтеглени", key='-ODL-', expand_x=True, expand_y=True), sg.Button("Изтегли", key='-DL-', expand_x=True, expand_y=True)]
    ]

window = sg.Window("Yt-dl-GUI",MainWinlayout, size=(380,200),
    ttk_theme=ttk_theme, use_ttk_buttons=True,
    element_padding=(0,0),
    margins=(0,0),
    font=FONTS,
    resizable=False,
    finalize=True
    )

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event=="Exit":
        break
        window.close()
        exit
    if event == 'Постави':
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
