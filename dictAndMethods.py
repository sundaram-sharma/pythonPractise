a = {}
b = {}
print(type(a))

dict1 = {
    "good":"Something is good",
    "Fine":"I am fine, how are you ?",
    "F1 car":"Hi baby, how are you ?"
}

print(dict1["good"])

marks = { "Sundaram": 34, "Herry": 40, "Simran": 90}

print(marks["Simran"])
marks["Priya"] = 34
print(marks)
print(marks.get("Priyanka Chopra"))
print(marks.keys())
print(marks.values())
print(marks.items())