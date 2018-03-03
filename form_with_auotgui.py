from shutil import copyfile
import pyautogui, os, sys
import pandas, time
import json
import csv
import argparse
import subprocess

# Information and argument required.
parser = argparse.ArgumentParser()
parser.add_argument("-t", dest="template_folder", default=None, help='Input the location of the template')
parser.add_argument("-i", action='store', dest="invoice_folder", default=None, help='Input the location of the invoice document')

args = parser.parse_args()

# Converting Invoicepdf to Invoice JSON

HOME = os.environ['HOME']
#base_dir = HOME + '/PycharmProjects/automation_demo/invoice2data-master/invoice2data/' '
#invoices_folder = '/Users/hithyshikrishnamurthy/Downloads/invoice2data-master/invoice2data/test/pdfs/'
#cmd = ['python3.5','/Users/hithyshikrishnamurthy/PycharmProjects/automation_demo/data_extraction.py',args.invoice_folder]
print('Extracting details from invoices')

src = HOME+'/Documents/invoice_details.csv'
dest = HOME+'/PycharmProjects/automation_demo/invoice_details.csv'
copyfile(src, dest)
time.sleep(5)
'''
print("Executing command:")
session = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
session_output = session.communicate()[0].decode('UTF-8')
'''
print('Created csv file')
#print('Starting Pyautogui switch to browser')
print('Launching automation to fill the form.')
time.sleep(3)

#Read the CSV file and get values.
df = pandas.read_csv('/Users/hithyshikrishnamurthy/Desktop/invoice_details.csv')
print(df)
(rows, columns) = (df.shape)

#Variables
#The image is a snip that contains the location of initial element.
image_loc = HOME +'/Desktop/train_image.png'
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

#Instructions
print('Press Ctrl-C to quit.')
#TODO: Get and print the mouse coordinates.

# Locating the first date tab on screen.
co_ordinates = pyautogui.locateOnScreen(image_loc)
if not co_ordinates:
    print('Unable to locate this element on screen. Please ensure the form is open')
    sys.exit()


try:
    for i in range(rows):
       #date, time = df['Invoice Date'][i].strip().split()
       date = df['Invoice Date'][i].strip()
       #year , month, day = date.strip().split('-')
       day, month, year = date.strip().split('/')
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
    print('\nFailed:Aborted.')
    sys.exit()
print('Success:Completed')
