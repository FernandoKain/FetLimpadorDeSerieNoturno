# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))


# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')

def backspace():
    pyautogui.press('backspace')

def delete():
    pyautogui.press('delete')



# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
time.sleep(0.5)

for i in range(2):
    for i in range(34):
        f2()
        up()
        up()
        delete()
        enter()

    for i in range(34):
        up()
    right()




