# !/usr/bin/env python3
# coding UTF-8
import math

class Employees:
    title = 'Cogniance employee'

    def __init__(self, full_name, position, sallary):
        self.full_name = full_name
        self.position = position
        self.sallary = sallary

    def split_name(self):
        return self.full_name.split(' ')

    def get_name(self):
        return self.split_name()[0]

    def get_surname(self):
        return self.split_name()[1]

    def sallary_for_month(self, num_of_month):
        return int(num_of_month) * int(self.sallary)

class Rectangles:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def perimeter(self):
        return (int(self.x) + int(self.y)) * 2

    def square(self):
        return int(self.x) * int(self.y)

class Dots:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.r = self.dist_to_00()
        self.angl = self.corner()

    def dist_to_00(self):
        return math.sqrt(int(self.x)**2 + int(self.y)**2)

    def corner(self):
        return math.atan(int(self.y) / int(self.x))
