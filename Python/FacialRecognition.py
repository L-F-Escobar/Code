import requests, json, base64, io
from base64 import b64encode
from PIL import Image
from io import BytesIO, StringIO

ENCODING = 'utf-8'



# Modify picture first then get ready for request call.
def convert_image_for_JSON_resize(image='', width=0, height=0):
        
    with open(image, 'rb') as f:
        with Image.open(f) as image:
            picture_resized = image.resize((width,height))
            buffer = io.BytesIO()
            picture_resized.save(buffer, format='PNG')
            img_data = buffer.getvalue()
        
    # second: base64 encode read data
    # result: bytes (again)
    base64_bytes = b64encode(img_data)
    
    # third: decode these bytes to text
    # result: string (in utf-8)
    base64_string = base64_bytes.decode(ENCODING)
    
    # Return data that is ready for a json call.
    return base64_string
    
    

# Request call happens here
def Comparision_Request(img1='', img2=''):
    # URL end point.
    url = 'https://api.authenticating.com/api/v1/comparePhotos'

    # HTTP Action.
    HTTP_action = 'POST'
    
    # Header Parameters.
    headers = {
        'Content-Type' : 'application/json',
        'Cache-Control': 'no-cache',
        'authKey' : "REMOVED_FOR_SECURITY"
    }

    # Body Parameters.
    body = {
        "accessCode" : "REMOVED_FOR_SECURITY",
        "img1" : img1,#"YOUR_BASE_64_ENCODED_IMAGE_GOES_HERE",
        "img2" : img2 #"YOUR_BASE_64_ENCODED_IMAGE_GOES_HERE"   
    }

    # Make HTTPS Request.
    response = requests.request(HTTP_action, url, json=body, headers=headers)

    # Return requests object of json data.
    responseBody = response.json()
    
    return responseBody
    


# Simply get the picture ready for the request call.
def nonmodified_converstion(image=''):  

    with open(image, 'rb') as open_file:
        encoded_image = base64.b64encode(open_file.read())
    
    base64_string = encoded_image.decode(ENCODING)
    
    return base64_string
  
    
    
def main():

    base64_str1_mod = convert_image_for_JSON_resize('bradpitt.jpg', 5000, 5000)
    base64_str2_mod = convert_image_for_JSON_resize('jon snow.png', 100, 100)# Face of Jon Snow.

    
    base64_str1_nonmod = nonmodified_converstion('bradpitt.jpg')
    base64_str2_nonmod = nonmodified_converstion('asianlady.jpg')


    response = Comparision_Request(base64_str1_mod, base64_str1_mod);
     
    for b in response:
        print(b, response[b])


main()
