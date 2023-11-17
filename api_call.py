import requests
import ast
import time

def call_api(img_path,api_endpoint):
    start=time.time()
    url = api_endpoint #"http://127.0.0.1:8000/detect"
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
    else:
        print("Request failed with status code:", response.status_code)

# Example usage
#call_api("C:/Users/pavan/Desktop/296.jpg")