num = (3,4,6)
print(num)

x,y,z = num
print(x)
print(y)
print(z)

print(x,y,z)

num = (3,6,7,3,23,4)
print(num)

x,y,*z = num
print(x,y,z)

x,*y,z = num
print(x,y,z)