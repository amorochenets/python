# !/usr/bin/env python3
# coding UTF-8
#
# class First:
#     color = None
#     def get_upper_color(self):
#         print(self.color.upper())
#
# fig = First()
# fig.color = 'green'
# fig.get_upper_color()
# print(type(fig))

class Employee:
    title = 'Cogniance employee'

    def __init__(self, name=None, surname=None):
        self.name = name
        self.surname = surname

    def set_name(self, name):
        self.name = name
    def set_surname(self, surname):
        self.surname = surname

    def full_name(self):
        print(self.name + ' ' + self.surname)

