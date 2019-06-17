# -*-coding: utf-8 -*-
"""
    @Project: python-learning-notes
    @File   : student.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-06-17 13:52:03
"""

from modules.custom_class.person import Person


class Student(Person):
    classes = ["A", "B"]

    def __init__(self, name, age):
        super(Student, self).__init__(name)
        self.age = age

    def print_student(self):
        print("name:{}".format(self.name))
        print("age :{}".format(self.age))
        print("classes :{}".format(self.classes))


if __name__ == "__main__":
    s = Student("S", 10)
    s.print_person()
    s.print_student()
