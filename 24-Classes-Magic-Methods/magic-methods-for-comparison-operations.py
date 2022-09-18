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

    def __gt__(self, otherstudent):
        return self.grades > otherstudent.grades

    def __ge__(self, otherstudent):
        return self.grades >= otherstudent.grades

    def __lt__(self, otherstudent):
        return self.grades < otherstudent.grades

    def __le__(self, otherstudent):
        return self.grades <= otherstudent.grades

    def __add__(self, otherstudent):
        return self.grades + otherstudent.grades

    def __sub__(self, otherstudent):
        return self.grades - otherstudent.grades

Didi = Student(math = 100, history = 90, writing = 80)
Awy = Student(math = 90, history = 105, writing = 70)

print(Awy < Didi)
print(Awy > Didi)
print(Awy <= Didi)
print(Awy >= Didi)
print(Awy >= Didi)
print(Awy + Didi)
print(Awy - Didi)
#print(abs(-5.56678))