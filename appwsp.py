import pyautogui as pg
import time

print('program se reinicio en 5 seg')
time.sleep(5)
for i in range(100):
	pg.write('i love you')
	time.sleep(0.5)
	pg.press('Enter')
