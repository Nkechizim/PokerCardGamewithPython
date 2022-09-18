class Teacher():
    def teach_class(self):
        print("Teaching stuff!!")

    def grab_lunch(self):
        print("Yum yum yum!!")

    def grade_test(self):
        print("F! F! F!")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("hurray!! I'm an author")
    
    def grade_test(self):
        print("A! A! A!")

teacher = Teacher()
cp = CollegeProfessor()

teacher.teach_class()
teacher.grab_lunch()
teacher.grade_test()
print()
cp.teach_class()
cp.grab_lunch()
cp.grade_test()
cp.publish_book()