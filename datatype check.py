student = {
    "name": "Karthika",
    "age": 22,
    "percentage": 85.5,
    "logged_in": True
}
print(type(student))
print(type(student["name"]))
print(type(student["age"]))
print(type(student["percentage"]))
print(type(student["logged_in"]))
if student["logged_in"]:
    print("Logged in")
else:
    print("Not logged in")