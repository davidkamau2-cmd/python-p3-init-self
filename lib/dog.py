#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt", age=0):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.breed}"