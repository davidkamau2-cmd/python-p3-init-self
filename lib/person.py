#!/usr/bin/env python3

class Person:
    def __init__(self, name="Guido", age=20):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
