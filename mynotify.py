import PySimpleGUI as sg

def move_DownR(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)-40, (screen_height - win_height)-40
    window.move(x, y)

def notify(title='', msg='', timeout=30, icon=''):
    layout = [
        [sg.T(title, size=(100,1))],
        [sg.Image(icon), sg.T(msg, expand_x=True, expand_y=True, size=(40,4))],
        #[sg.P(), sg.B("Ok", key='Exit')]
        ]

    window = sg.Window('title',layout,
        size=(350,80),
        element_padding=(0,0),
        margins=(0,0),
        resizable=False,
        finalize=True,
        no_titlebar=True,
        grab_anywhere=True,
        location = (sg.Window.get_screen_size()[0]-370,sg.Window.get_screen_size()[1]-130),
        auto_close = True,
        auto_close_duration = timeout,
        )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
            window.close()
            exit

if __name__ == "__main__":
    notify('Test title!', 'test message', 5)
