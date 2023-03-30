'''font size 12'''
import webbrowser
import time
import pyautogui as gui
from miscellenous import *
for i in range(36,37):
    for j in range(1,52):
        if i!=j:
            webbrowser.open("'http://fare.bmrc.co.in/'")
            time.sleep(10)
            ''' find the cursor position and size of screen'''
            # print(gui.size())
            # print(gui.position())

            ''' selecting source stop'''
            gui.click(702, 225) # from station
            gui.press("down", presses=i)
            gui.press("enter")
            time.sleep(5)
            # #
            # # ''' selecting destination stop'''
            gui.click(700, 272) # to station
            gui.press("down", presses=j)
            gui.press("enter")
            time.sleep(5)
            #
            ''' selecting the source stop name'''
            gui.mouseDown(button='left', x=650, y=234)
            gui.dragTo(557, 202, 1, button='left')
            gui.mouseUp()
            time.sleep(5)
            gui.hotkey('ctrl', 'c')

            ''' minimise the webpage'''
            time.sleep(1)
            gui.click(1775, 17)

            ''' open miscellenous file'''
            time.sleep(1)
            gui.click(193, 90)
            ''' write source name in miscellenous file'''
            gui.write("'''")
            gui.hotkey('ctrl', 'v')
            gui.press("right", presses=3)
            gui.write(",")

            ''' maximize webpage'''
            time.sleep(5)
            gui.click(586, 1060)

            ''' selecting the destination stop name'''
            gui.mouseDown(button='left', x=722, y=292)
            gui.dragTo(557, 253, 1, button='left')
            gui.mouseUp()
            time.sleep(1)
            gui.hotkey('ctrl', 'c')

            ''' minimise the webpage'''
            time.sleep(1)
            gui.click(1775, 17)

            ''' open miscellenous file'''
            time.sleep(1)
            gui.click(193, 90)

            ''' write destination name in miscellenous file'''
            gui.write("'''")
            gui.hotkey('ctrl', 'v')
            gui.press("right", presses=3)
            gui.write(",")

            ''' maximize webpage'''
            time.sleep(1)
            gui.click(586, 1060)

            ''' selecting the fare'''
            time.sleep(5)
            gui.mouseDown(button='left', x=921, y=321)
            gui.dragTo(894, 319, 1, button='left')
            gui.mouseUp()
            time.sleep(1)
            gui.hotkey('ctrl', 'c')

            ''' close the webpage'''
            time.sleep(1)
            gui.click(340, 19)

            ''' open miscellenous file'''
            time.sleep(1)
            gui.click(193, 90)

            ''' write fare in miscellenous file'''
            gui.write("'''")
            gui.hotkey('ctrl', 'v')
            gui.press("right", presses=3)
            gui.write(",")










