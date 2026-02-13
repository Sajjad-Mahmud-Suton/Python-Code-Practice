students  = ["Sajjad","Mahmud", "Suton" ]
print(students)
print(students*3)
print(students[2])
print(students+["ABC",22])
print("XYZ" in students)
print("XYZ" not in students)

print(len(students))
students.append("Shakib")
print(students)

students.insert(2,"BD")
print(students)
students.remove("Shakib")
print(students)

students.sort()
print(students)

students.reverse()
students1=students.copy()
print(students1)

students1.pop()

pos = students1.index("Sajjad")
print(pos)