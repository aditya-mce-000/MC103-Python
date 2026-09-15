student = {"Name": "Aditya", "Roll": "26/B4/019", "Branch": "MCE", "College":"DTU"}

print(student.items())
print(student.keys())
print(student.values())

student['City'] = "Delhi"
print(student)

student["Branch"] = "CSE"
print(student)

del student["College"]
print(student)