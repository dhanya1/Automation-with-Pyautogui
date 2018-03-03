# import the necessary packages
import PIL
from PIL import Image, ImageEnhance
import pytesseract
import argparse
import os,sys
import cv2 as cv
import numpy as np
import subprocess
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = ap.parse_args()

# load the image and convert it to grayscale and resize the image.
'''
basewidth = 300
img = Image.open(args.image)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized_image.png')

# Change the contrast level
#scale_value=scale1.get()
contrast = ImageEnhance.Contrast(img)
#contrast_applied=contrast.enhance(2)

filename = 'output.png'
img.save('output.png')
'''
# Reduce background noise and binraize the image
img = Image.open(args.image)
width, height = img.size
image = cv.imread(args.image,0)
#os.remove(filename)
#gray = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

# Reducing noise and making text prominant
gray = cv.threshold(image, 0, 255,cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid())
cv.imwrite(filename, gray)

# Convert file to pdf.
pdfname = "{}.pdf".format(os.getpid())
cmd = 'convert -quality 100 '+filename+' '+pdfname
os.remove(filename)
'''
# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle

if angle < -45:
	angle = -(90 + angle)
 
# otherwise, just take the inverse of the angle to make
# it positive

else:
	angle = -angle

# rotate the image to deskew it
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)



sys.exit()
text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
#print(text)
im = Image.open(filename)
print(im.info)
sys.exit()
text = image_to_string(im)
text = image_file_to_string(args.image)
text = image_file_to_string(image_file, graceful_errors=True)
print("=====output=======\n")
print(text)
'''
