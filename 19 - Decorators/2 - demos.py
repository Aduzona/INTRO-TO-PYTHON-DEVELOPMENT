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

sample()