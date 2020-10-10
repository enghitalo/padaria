import pyautogui
import time
import os
import subprocess
import pandas as pd
import pyperclip
import pydirectinput

x=0
y=0

# # os.startfile('C:\WINDOWS\system32\mspaint.exe')


# # subprocess.Popen("%s %s" % ("C:\WINDOWS\system32\mspaint.exe",
# #                            r'C:/Users/hital/Desktop/padaria/imagem.png'))

# # subprocess.Popen("%s %s" % ("C:\WINDOWS\system32\mspaint.exe",
# #                             r'C:/Users/RODRIGUES/Desktop/padaria/login.png'))
# # os.startfile('C:\Getway\Profit\GWProfit.exe')

time.sleep(1)
pyautogui.confirm('Deseja iniciar a aplicação?')
print(pyautogui.position())
pydirectinput.moveTo(547, 231) # Move the mouse to the x, y coordinates 100, 150.
pydirectinput.click()
pyautogui.moveTo(647,231,duration=1)
pyautogui.click()
print(pyautogui.position())


# time.sleep(1)

# # pyautogui.hotkey('win', 'up')


# # (x, y) = pyautogui.center(pyautogui.locateOnScreen(
# #     'red.png'))
# # pyautogui.click(x, y)

# # (x, y) = pyautogui.center(pyautogui.locateOnScreen(
# #     'letra.png'))
# # pyautogui.click(x, y)

# #pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)


dfs = pd.read_excel('padaria_barcodes.xlsx', sheet_name='db', dtype='str')
# dfs = [[0, 0, 0, 0],[0, 0, 0, 0]]
# # print(dfs.values)

# (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#     'user.png'))
# pyautogui.click(x+50, y, clicks=2)
# pyautogui.hotkey('h')
# pyautogui.typewrite('HITALO')
# # pyautogui.hotkey('esc')

# (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#     'senha.png'))
# pyautogui.click(x+50, y)
# pyautogui.typewrite('1234')
# # pyautogui.hotkey('esc')

# (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#     'ok.png'))
# pyautogui.click(x, y)

# # (x, y) = pyautogui.center(pyautogui.locateOnScreen(
# #     'faturamento.png'))
# # pyautogui.click(x-10, y)

# (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#     'emissaonf.png'))
# pyautogui.click(x, y)

# pyautogui.hotkey('f2')
# time.sleep(1)

# for itens in dfs.values:

#     print(str(itens[1]))
#     print(float(itens[2]))

#     x = 0
#     y = 0

#     (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#         'barra.png'))
#     pyautogui.click(x-20, y+20)
#     pyautogui.write(str(itens[1]))
#     pyautogui.hotkey('enter')
#     pyautogui.hotkey('enter')
#     # pyautogui.hotkey('esc')

#     (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#         'cod Tributacao.png'))
#     pyautogui.click(x-5, y+20)
#     pyautogui.hotkey('backspace')
#     pyautogui.hotkey('backspace')
#     pyautogui.hotkey('backspace')
#     pyautogui.hotkey('backspace')
#     pyautogui.write("041")
#     pyautogui.hotkey('enter')
#     # pyautogui.hotkey('esc')

#     (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#         'preco Unit.png'))
#     pyautogui.click(x, y+20, clicks=2)
#     pyautogui.hotkey('ctrl', 'c')
#     # pyautogui.hotkey('esc')
#     # pyperclip.copy("13")

#     (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#         'quantidade.png'))
#     pyautogui.click(x, y+20)
#     pyautogui.write(str(float(itens[2])/float(pyperclip.paste())))
#     # pyautogui.hotkey('esc')

#     (x, y) = pyautogui.center(pyautogui.locateOnScreen(
#         'preco Unit.png'))
#     pyautogui.click(x, y+20)
#     pyautogui.write(str(float(pyperclip.paste())/2))
#     # pyautogui.hotkey('esc')
#     pyautogui.hotkey('alt', 's')

# pyautogui.hotkey('alt', 'f')
# # pyautogui.hotkey('alt', 'f4')
