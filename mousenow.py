import pyautogui, os, sys
import pandas

#Variables
HOME = os.environ['HOME']

#The image is a snip that contains the location of initial element.
image_loc = HOME +'/Desktop/train_image.png'
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
try:
    for i in range(rows):
       day , month, year = df['Invoice Date'][i].strip().split('/')
       #clicking on the element and passing values
       # Find the center of the element located
       ele_center = pyautogui.center(co_ordinates)
       pyautogui.click(ele_center)
       pyautogui.typewrite(day)
       pyautogui.typewrite('\t')
       pyautogui.typewrite(month)
       pyautogui.typewrite('\t')
       pyautogui.typewrite(year)
       pyautogui.typewrite('\t')
       pyautogui.typewrite(str(df['Invoice Number'][i]))
       pyautogui.typewrite('\t')
       pyautogui.typewrite(str(df['Supplier Name'][i]))
       pyautogui.typewrite('\t')
       pyautogui.typewrite(str(df['Net Amount'][i]))
       pyautogui.typewrite('\t')
       pyautogui.typewrite(str(df['VAT'][i]))
       pyautogui.typewrite('\t')
       pyautogui.typewrite(str(df['Gross Amount'][i]))
       pyautogui.typewrite('\t')
   
       #Submit the form
       pyautogui.press('enter')

except KeyboardInterrupt:
    print('\nDone.')

