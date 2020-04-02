# coding:utf-8
from abc import ABCMeta, abstractmethod


class Person(object):
    __meta_class__ = ABCMeta

    def __init__(self, **kwargs):
        self.age = kwargs.get("age")
        self.name = kwargs.get("name")

    def hello(self):
        print ("hello, my name is {0}, and my age is {1}".format(self.name, self.age))

    @abstractmethod
    def say(self):
        pass


class Student(Person):
    def __init__(self, **kwargs):
        super(Student, self).__init__(**kwargs)
        self.school = kwargs.get("school")

    def say(self):
        print ("my school is ", self.school)

stu = Student(name="wangming", age=19, school="Henan Politecnic University")
stu.hello()
stu.say()

try:
    pass
except s:Exception:
    pass
finally:
    pass
