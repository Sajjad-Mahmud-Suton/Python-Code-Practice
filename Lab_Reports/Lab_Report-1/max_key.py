data = {
    "Sajjad": 85,
    "Mahmud": 92,
    "Suton": 78,
    "Sajid": 95,
    "Esha": 88
}
max = list(data.keys())[0]
for key in data:
    if data[key] > data[max]:
        max = key

print(f"The person with the highest score is {max} with a score of {data[max]}")