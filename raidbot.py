import pyautogui
import time
import click
import keyboard
#pyautogui.displayMousePosition()
# X:  922 Y:  997 RGB: (166, 211,  57)

while keyboard.is_pressed('q') == False:
    #Tempo de fuga1
    time.sleep(1)

    #Verificando pixel para clicar
    if pyautogui.pixel(922,997)[1] == 211:
        #Clicando
        click(922,997)