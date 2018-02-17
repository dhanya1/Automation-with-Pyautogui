import pyautogui, os, sys
from pandas import read_excel

#Variables
HOME = os.environ['HOME']
image_loc = HOME +'/Desktop/train_image'
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

#Instructions
print('Press Ctrl-C to quit.')
#TODO: Get and print the mouse coordinates.

# Locating the first date tab on screen.
co_ordinates = pyautogui.locateOnScreen(image_loc)
if not co_ordinates:
    print('Unable to locate this element on screen. Please ensure the form is open')
    sys.exit()

#Clicking on the element and passing values
try:
   # Find the center of the element located
   ele_center = pyautogui.center()

   #Click on the center of the element
   pyautogui.click(ele_center)

   pyautogui.typewrite('\t')
   pyautogui.typewrite('Hello world')
   pyautogui.typewrite('\t')
   pyautogui.typewrite('Dhanya')
   positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

   #Submit the form
   pyautogui.press('enter') 

except KeyboardInterrupt:
    print('\nDone.')
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)
