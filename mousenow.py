import pyautogui, os, sys
import pandas

#Variables
HOME = os.environ['HOME']
image_loc = HOME +'/Desktop/train_image.png'
# mouseNow.py - Displays the mouse cursor's current position.
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

#Read the CSV file and get values.
df = pandas.read_excel('/Users/hithyshikrishnamurthy/Desktop/invoice_details.xlsx')
(rows, columns) = (df.shape)
day , month, year = df['Invoice Date'][0].strip().split('/')
#clicking on the element and passing values
try:
   # Find the center of the element located
   ele_center = pyautogui.center(co_ordinates)
   pyautogui.click(ele_center)
   pyautogui.typewrite(day)
   pyautogui.typewrite('\t')
   pyautogui.typewrite(month)
   pyautogui.typewrite('\t')
   pyautogui.typewrite(year)
   pyautogui.typewrite('\t')
   pyautogui.typewrite(str(df['Invoice Number'][0]))
   pyautogui.typewrite('\t')
   pyautogui.typewrite(str(df['Supplier Name'][0]))
   pyautogui.typewrite('\t')
   pyautogui.typewrite(str(df['Net Amount'][0]))
   pyautogui.typewrite('\t')
   pyautogui.typewrite(str(df['VAT'][0]))
   pyautogui.typewrite('\t')
   pyautogui.typewrite(str(df['Gross Amount'][0]))
   pyautogui.typewrite('\t')
   
   #Submit the form
   pyautogui.press('enter')
   positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)


except KeyboardInterrupt:
    print('\nDone.')
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)

