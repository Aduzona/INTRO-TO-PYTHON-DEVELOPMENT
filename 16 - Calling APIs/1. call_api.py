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
# print(subscription_key)

# You need to update the vision_service_address to the address of
# your Computer Vision service
#vision_service_address = "https://westeurope.api.cognitive.microsoft.com/vision/v3.0/"
vision_service_address ="https://diegopythonimageanalyzer.cognitiveservices.azure.com/vision/v3.0/"

# Add the name of the function we want to call to the address
address =vision_service_address + "analyze"

# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
# These are the parameters we want to pass into the function
parameters = {'visualFeatures':'Description,Color','language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path ="./TestImages/PolarBear.jpg"
image_data = open(image_path,"rb").read()

# According to the documentation for the analyzer image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octer-stream when you pass in an image directly
# while Content-Type is application/json if it is being passed inform of json
# the key as it is being displayed here is not the best practice
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-key': SUBSCRIPTION_KEY }

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
# print(json.dumps(results))

# getting values in JSON
# Just like in folder color contains dominatColorBackground
print(results['color']['dominantColorBackground'])

# If you have value in a list, e.g description, tags list of several values
# print(results['description']['tags'][0])

# if you want all of the tags to comeout, use a loop.
for item in results['description']['tags']:
    print(item)

# Apart from reading a JSON, you might be requeired to create a JSON to parse to a web service
# You can create "Key":"value" JSON objects from dictionary
