# Challenge #1
# Create an Azure Custom Vision Service 
# Analyze an image and return the JSON describing the image.
# call_api.py is a completed solution, but it will not run unless
# you do the following:
#   Create a Custom Vision Service in Azure
#   Update the Key 
#   Update the address of your service
#   Update the image file and location

# Bonus Challenge 
# Your skills are growing, it's time to start trying to figure things out on your own
# based on documentation. You have already called one function of the Computer Vision Service
# Now try calling another
# Instead of calling the analyze method of the service, try calling the OCR method 
# Here is some helpful documentation
# https://docs.microsoft.com/azure/cognitive-services/Computer-vision/concept-recognizing-text#ocr-optical-character-recognition-api
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fc
# Use the documentation to figure out
#    The correct function name for the address
#    The parameters you need to pass the function
#    The HTTP Headers required    
# Pass in an image containing text
# The JSON returned will contain the string of text in the image
# Good luck!

# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python
import requests # easier for http call from python

# We will need the json library to read the data passed back
# by the web service
import json

# You need to update the SUBSCRIPTION_KEY to
# the key for your Computer Vision Service
from dotenv import  load_dotenv
load_dotenv()
import os
SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')

# You need to update the vision_service_address to the address of
# your Computer Vision service
#vision_service_address = "https://westeurope.api.cognitive.microsoft.com/vision/v3.0/"
vision_service_address ="https://diegopythonimageanalyzer.cognitiveservices.azure.com/vision/v3.0/"

# Add the name of the function we want to call to the address
# OCR: Optical Character Recognition
#  Dectects texts in an image and extracts the recognized characters into
# a machine-usable character stream.
address =vision_service_address + "ocr"

# There are 2 parameters needed, language and detectionOrientation
# dectectOrientation is if the image is upside down, it need to currect it first
# parameters = {'language':'en','dectectOrientation':'true'}
parameters = {'language':'en'}

# Open the image file to get a file object containing the image to extract text from
image_path ="./TestImages/Prayer.jpg"
image_data = open(image_path,"rb").read()

# According to the documentation for the ocr image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octer-stream when you pass in an image directly
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-key': SUBSCRIPTION_KEY }

# According to the documentation for the ocr image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))