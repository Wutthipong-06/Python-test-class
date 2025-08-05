student = {"name":"Alice", "age":"18", "grade":"A"}
print(student)
print(student['name'])
print(student['age'])
print(student["grade"])

student = dict(name="Alice", age="18", grade="A")
print(student)

student = dict([("name", "Alice"), ("age", "18"), ("grade", "A")])
print(student)