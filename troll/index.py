#automatizar msg de ofensa para meu amigo
import pyautogui
import time

pyautogui.PAUSE = 2

#passo 1: entrar no instagram dele
pyautogui.press('win')
pyautogui.write('navegador opera')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://www.instagram.com/junqueiira___/')
pyautogui.press('enter')
time.sleep(10)

#passo 2: entrar na DM
pyautogui.click(x=1332, y=212)  # coordenadas do icone de DM

#passo 3: enviar msg de ofensa
time.sleep(2)
for i in range(20):  # enviar 20 mensagens
    pyautogui.write('iiiiiiiiiiiiiiiiiiiiiiiiihhhhhhhh ta com essa daiiiiiiiiiiiiiiiiiiiiiiiiiiiiii??????????????????')
    pyautogui.press('enter')