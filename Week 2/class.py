class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}."

    def update_grade(self, new_grade):
        self.grade = new_grade


student1 = student("Alice", 20, "A")

print(student1.name)
print(student1.age)
print(student1.grade)

print(student1)
student1.update_grade("A+")

print(student1)