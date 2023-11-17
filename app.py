from pywebio.input import *
from pywebio.output import *
from api_call import call_api
from boundinbox import draw_rectangle
from PIL import Image, ImageDraw, ImageFont

image_path=input("Enter Image Address",type=TEXT)
data=call_api(str(image_path)) #"C:/Users/pavan/Desktop/296.jpg"
put_text("OUTPUT")
img = Image.open(image_path) 
width = img.width 
height = img.height 
print("width",width)
print("height",height)
for i in range(len(data)):
    label =str.upper(data[str(i)]["name"])+" : "+data[str(i)]["confidence"]
    put_text(label)
    #put_text("coordinates: "+data[str(i)]["xmin"],data[str(i)]["ymin"],data[str(i)]["xmax"],data[str(i)]["ymax"])
    xmin=float(data[str(i)]["xmin"])*width
    ymin=float(data[str(i)]["ymin"])*height
    xmax=float(data[str(i)]["xmax"])*width
    ymax=float(data[str(i)]["ymax"])*height
    print(xmin,ymin,xmax,ymax)
    draw_rectangle(image_path='C:/Users/pavan/Desktop/296.jpg', xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax, label=label,label_font_size=2.7,i=i)

img = Image.open('./image_with_rectangle.jpg') 
put_image(img,width='1000px')