x = 50

def func():
    '''test global'''
    global x
    x = 2


func()
print('x is ', x)
print(func.__doc__)
