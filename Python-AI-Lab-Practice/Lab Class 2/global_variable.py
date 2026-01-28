x = "awesome"
def myfunc():
  print("Python is " + x)
  
myfunc()

x = "fantastic"
def myfunc():
    x="great"
    print("Python is " + x)
myfunc()

print("Python is " + x)

z = "incredible"
def myfunc():
    global z
    z = "amazing"
    print("Python is " + z)
myfunc()
print("Python is " + z)