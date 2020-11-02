# IMPORTS 

import platform, distro
from PIL import Image, ImageDraw, ImageFont

kernelpre = "カーネル :"
kernelversion = platform.release().upper()
node = distro.id().upper()
system = platform.system().upper()

image = Image.open('background.png')
draw = ImageDraw.Draw(image)

# FONTS 
font = ImageFont.truetype('HanaMinA.ttf', size=20) # ttf-hanazono
font2 = ImageFont.truetype('DejaVuSerifCondensed.ttf', size=55) # ttf-dejavu

kernel = kernelpre + kernelversion
distro = node +' '+ system

W,H = 1920, 1080
w,h = font.getsize(kernel)
draw.text(((W-w)/2,(H-h)/2), kernel, font=font, fill="black")

X,Y = 1920, 1080
x,y = font2.getsize(distro)
draw.text(((X-x)/2,(Y-y)/2-50), distro, font=font2, fill=(168,166,174))
 
image.save('bg.png')
