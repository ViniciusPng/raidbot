import pyautogui
import time
import click
import keyboard
import win32api, win32con
#pyautogui.displayMousePosition()

# Botão de Rerun
# X:  922 Y:  997 RGB: (166, 211,  57)
# X:  947 Y:  995 RGB: (203, 240, 103)]
# X:  730 Y:  984 RGB: (203, 240,  96)

# Botão de X de mensagem
# X: 1376 Y:  216 RGB: (201,  44,  45)
# X: 1380 Y:  222 RGB: (212,  53,  54)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    #Verificando pixel para clicar
    if pyautogui.pixel(730,984)[1] == 211 or pyautogui.pixel(730,984)[1] == 240:
        #Clicando
        time.sleep(1)
        click(730,984)