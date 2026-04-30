import requests

url = "http://127.0.0.1:8000/predict"

from PIL import Image

# We will create valid solid-color images to pass the PIL Image.open() validation
img1 = Image.new('RGB', (100, 100), color = 'red')
img1.save('test1.jpg')

img2 = Image.new('RGB', (100, 100), color = 'blue')
img2.save('test2.jpg')

files = [
    ("files", ("test1.jpg", open("test1.jpg", "rb"), "image/jpeg")),
    ("files", ("test2.jpg", open("test2.jpg", "rb"), "image/jpeg"))
]

try:
    response = requests.post(url, files=files)
    print("Status Code:", response.status_code)
    print("Response payload:", response.json())
except Exception as e:
    print("Connection Error. Is the uvicorn server running?")
    print(e)
