jatri = {
    "name": "Rahim",
    "boyosh" : 25,
    "seat": "A1"
}

# print(jatri["name"])
# print(jatri["seat"])

jatri["phone"] = "0152654"

# print(jatri["phone"])

student = {
    "name": "Rakib",
    "age": "24",
    "city": "Tangail"
}
# print(student)
# print(student["name"])

student["city"] = "Dhaka" #change value
student["grade"] = "A" #New key value added
# print(student)

for key in student:
    print(key,":",student[key])
    