import requests
import ast
import time

def call_api(img_path):
    start=time.time()
    url = "http://127.0.0.1:8000/detect"
    files = {"img": open(img_path, "rb")}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print("Request was successful!")
        end=time.time()
        print("Time taken: ",end-start)
        #print(type(response.text))
        data=ast.literal_eval(response.text)
        print(data)
        return data
        for i in range(len(data)):
            print(str.upper(data[str(i)]["name"])+" : "+data[str(i)]["confidence"])
            print("coordinates: "+data[str(i)]["xmin"],data[str(i)]["ymin"],data[str(i)]["xmax"],data[str(i)]["ymax"])
    else:
        print("Request failed with status code:", response.status_code)

# Example usage
#call_api("C:/Users/pavan/Desktop/296.jpg")