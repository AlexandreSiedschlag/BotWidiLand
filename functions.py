import win32api, win32con
from time import sleep


def clicar(posicaoX, posicaoY):
    def click(x,y, duration=30): 
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        sleep(duration / 1000)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        sleep(0.3)    
    if isinstance(posicaoX, list):
        for item in posicaoX:
            x=int(item[0])
            y=int(item[1])
            click(x,y)
            sleep(1)
    if isinstance(posicaoX, tuple):
        x=int(posicaoX[0])
        y=int(posicaoX[1])
        click(x,y)
        sleep(1)
    if isinstance(posicaoX, int):
        if isinstance(posicaoY, int):
            x = posicaoX
            y = posicaoY
            click(x,y)
            sleep(1)

