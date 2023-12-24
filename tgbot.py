import pyautogui
import time
import click
import keyboard
import win32api, win32con

# Botões
# Botão 1
# X: 1271 Y:  621 RGB: ( 31, 171, 208)

# Botão 2
# X: 1067 Y:  982 RGB: (156, 208,  31)

# Botão 3
# X:  882 Y:  986 RGB: (240,  97, 105)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    #Verificando pixel para clicar
    #botão 1
    if pyautogui.pixel(1271,621)[2] == 208:
        #Clicando
        time.sleep(1)
        click(1271,621)
    
    #botão 2
    if pyautogui.pixel(1067,982)[1] == 208:
        #Clicando
        time.sleep(1)
        click(1067,982)
        
    #botão 3
    if pyautogui.pixel(882,986)[0] == 240:
        #Clicando
        time.sleep(1)
        click(882,986)