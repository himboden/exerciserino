from module import *
from moduleElement import *

class Student(object):

    modules = []
    grades = {}

    def __init__(self, name):
        self.name = name

    def add_module(self,module):
        Student.modules.append(module)
        Student.grades[module]=module.get_grade()

    def get_list_modules(self):
        for whatever in Student.modules:
            print("Modules of {}:".format(self.name))
            print("{}".format(whatever.get_title()))

    def get_grades(self):
        for i_hope_this_doesnt_make_it_more_complicated_for_you_to_correct_if_it_does_im_sorry in Student.grades:
            print("\nGrades of {}:".format(self.name))
            print("{}: {}".format(i_hope_this_doesnt_make_it_more_complicated_for_you_to_correct_if_it_does_im_sorry.get_title(), Student.grades[i_hope_this_doesnt_make_it_more_complicated_for_you_to_correct_if_it_does_im_sorry]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6