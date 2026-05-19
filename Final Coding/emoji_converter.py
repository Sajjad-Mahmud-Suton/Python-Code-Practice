text = input(">> ")
words = text.split(' ')

emoji = {
    ":)" : "😃",
    ":(" : "😞"
}
output = " "
for char in words:
    output += emoji.get(char,char) + " "

print(output)