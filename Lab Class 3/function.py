

print("regular arguments:   ")
def my_function(name):
    print("Name:", name)
my_function("Sajjad")
my_function("Mahmud")
my_function("Suton")

print("Arbitary arguments:   ")
def my_function(*names):
    print("Names:", names[2])
    print("Names:", names[1])
    print("Names:", names[0])

my_function("Sajjad", "Mahmud", "Suton")

print("Sent arguments with the key value syntax:   ")

def my_function(name3, name2, name1):
    print("Name:", name1)
    print("Name:", name2)
    print("Name:", name3)
my_function(name1="Sajjad", name2="Mahmud", name3="Suton")

print("Arbitrary keyword arguments:   ")
def my_function(**names):
    print("First Name:", names["fname"])
    print("Middle Name:", names["midname"])
    print("Last Name:", names["lname"])
    
    my_function(fname="Sajjad", midname="Mahmud", lname="Suton")
    
print("list as an argument:    ")
fruits = ["apple", "banana", "cherry"]
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function(fruits)

print ("returning values:   ")
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))