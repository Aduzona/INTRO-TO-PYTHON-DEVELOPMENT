# Decorators

[Decorators](https://www.python.org/dev/peps/pep-0318/) are similar to attributes in that they add meaning or functionality to blocks of code in Python. They're frequently used in frameworks such as [Flask](http://flask.pocoo.org/) or [Django](https://www.djangoproject.com/). The most common interaction you'll have with decorators as a Python developer is through using them rather than creating them.

``` python
# Example decorator
@log(True)
def sample_function():
    print('this is a sample function')
```

# Programming Components 
Objects
- Nouns
- Data constructs
e.g OS can be an object

Functions/Methods
- Verbs
- Actions
e.g getenv is something that we can do, We can go get environmental variable.

Decorators
They allow us to ass additional meaning to our code, that way e.g if we are running it inside flask, it knows what it is we are traing to tell it or when it should call different things we created
- Adjectives
- Add additional functionality to code
- Common in frameworks e.g
 - Django
 - Flask

# Using a decorator
``` python
# Snippet from Flask
# register https://myserver/api/products

@route('api/products')
def get_products:
    # code to list from database
    pass
```

When we are creating a web application with python, we are allowing people to call methods/functions that we've created.
The way they are going to do that is to specify some particular URL, so if you are thinking of a pubic api like register https://myserver/api/products .
When a user navigates to this url, @route('api/products') call get_products() function

@route is a route registration, 

# Creating a decorator

``` python
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper

# if some one uses decorator logger, call the function wrapper() returning wrapper
# in the middle fun() the function sample() will be called.
@logger
def sample():
    print('-- Inside sample function')

'''
OUTPUT

Logging execution
-- Inside sample function
Done logging

'''
```

* The most common time we create decorator on our own is when creating our own framework which is rear. 
so the most common time is when we will use them 

