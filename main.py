#Resizes an image and keeps aspect ratio. Set mywidth to the desired with in pixels.

import PIL
from PIL import Image

mywidth = 1614

img = Image.open('C:/Users/parth/OneDrive/Documents/IMagecompressor/1.jpg')//imagepath
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('C:/Users/parth/OneDrive/Documents/IMagecompressor/11.jpg')//new image path
