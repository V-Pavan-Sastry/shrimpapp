from pywebio.input import *
from pywebio.output import *
from api_call import call_api
from boundinbox import draw_rectangle
from PIL import Image
import time
import cv2
flag=True
api_endpoint=''
def upload():
    f = file_upload("Upload a file")    
    print(f)              
    open('./assets/'+'captured_img.jpg', 'wb').write(f['content'])
    open('./assets/'+'result.jpg', 'wb').write(f['content'])
    result()  
def click():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()          
    cv2.imwrite('./assets/captured_img.jpg', frame)
    cv2.imwrite('./assets/result.jpg', frame)
    put_text("Clicking a pick ...")
    result()
def display():
    global flag
    global api_endpoint
    if flag==True:
        api_endpoint=str(input("Enter API End Point : ",type=TEXT))
        flag=False
    put_button('Upload an Image',onclick=upload)
    put_button('Click an Image',onclick=click)
def result():
    put_text("Loading . . . ")
    global api_endpoint
    image_path="./assets/captured_img.jpg"
    data=call_api(img_path=str(image_path),api_endpoint=api_endpoint) #"C:/Users/pavan/Desktop/296.jpg"
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
        draw_rectangle(image_path='./assets/captured_img.jpg', xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax, label=label,label_font_size=2.7)

    img = Image.open('./assets/result.jpg') 
    put_image(img,width='800px')
    put_text(" ")
    put_button("Try Again", onclick=display)

display()
