x = "awesome"

def myfunc():
    print("Python is " + x)
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
