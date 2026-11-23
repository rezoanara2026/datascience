student = {"name": "Amina", "age": 20, "score": 78}
student["score"]= 85
student["major"]= "AMDS"
removed_key=student.pop("age")
print("Updated student dictionary:", student)
print("Removed key:", removed_key)