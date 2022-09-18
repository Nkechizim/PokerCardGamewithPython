class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing 

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self, otherstudent):
        return self.grades == otherstudent.grades

Ify = Student(90, 90, 90)
Didi = Student(math = 100, history = 90, writing = 80)
Awy = Student(math = 40, history = 45, writing = 50)

print(Ify.grades)
print(Didi.grades)
print(Awy.grades)
print(Ify == Awy)
print(Awy != Ify)
print(Ify == Didi)
print(Ify != Didi)
print(Awy == Didi)
print(Awy != Didi)