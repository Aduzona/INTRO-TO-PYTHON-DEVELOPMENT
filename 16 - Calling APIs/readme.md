# What is a web service?

When a developer wants to share the functionality of a function but not the actual code in the program, they can place the function on a web server.

A programmer with the address of that function on the web server and the required permissions can call the function.

This is called a web service

# What is an API

You can't call a function unless you know the function name and the required parameters

When you create a web service you create an Application Programming Interface (API)

The API defines the function names and parameters so others know how to call your function.

* Example of function we will call from cognitive service
analyze(visualfeatures,details, language)

# Calling APIs

You can call functions called by other programs hosted on web servers. [Microsoft Azure Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/?WT.mc_id=python-c9-niner) contain a number of APIs you can call from your code to add intelligence to your apps and websites.

In the code example you call the [Analyze Image](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa0) function of the [Computer Vision](https://docs.microsoft.com/azure/cognitive-services/computer-vision/?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)

# Keys
- Keys allow me to track which users have permission to use my web service.

* A developer signs up on my web site, or buys a lincense for my software and is provided a unique key

* When the developer calls my web service they provide their unique key and I am able to verify the key has been approved for calls to my web service

This key is unique for everyone who has access.

Requirements for calling an API:

- [API Key](https://azure.microsoft.com/try/cognitive-services/?WT.mc_id=python-c9-niner) to give you permission to call the API
- Address or Endpoint of the service
- function name of method to call as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)
- function parameters as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)
- HTTP Headers as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)


# Messaging Standard

- There is a standard for sending messages across the web
Hypertext Transfer Protocol(HTTP) is a standard protocol for sending messages across the web

* GET
    * Pass values in query string only
        * Special characters must be "escaped"
        * Limited amount of data
* POST
    * Pass values in query string and body
        * No need to escape special characters if passed in body.
        * Can pass large anounts of data, including images, in body.
    e.g parsing a file
E.g in the documentation analyze function from cognitive services uses POST: [Cognitive Services](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa )


# request libraries

This simplifies HTTP calls from Python code
Simplifies making a post for a get call
- Import the request library, You will have to pip install first.
- call:
requests.post(address,
              http_headers,
              function_parameters,
              message_body)
   - address: what server is this on? http/contoso/analyze. you get this from the documentation on the web service.
   - http_headers: content-type, API key (Subscription key)
   - function_parameters: visualfeatures,details, language.
   - message_body: That is the image that I want to pass in. We know this from the documentation.


   # Start

   - Create an account:
   [Create account](https://docs.microsoft.com/en-ca/azure/cognitive-services/cognitive-services-apis-create-account#single-service-subscription)