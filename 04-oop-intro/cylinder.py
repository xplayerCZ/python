import math
import random


class Cylinder:
    default_height = 4
    default_radius = 1
    default_color = "red"

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.color = self.default_color


    def base(self):
        return (self.radius ** 2) * math.pi

    def volume(self):
        return self.base() * self.height

    def __str__(self):
        return f'Cylinder(radius={self.radius}, height={self.height}, color={self.color})'

    def __eq__(self, other):
        return self.radius == other.radius and self.height == other.height

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __add__(self, other):
        if self.radius != other.radius:
            return Cylinder(0, 0)
        return Cylinder(self.radius, self.height + other.height)

    @classmethod
    def random_cyl(cls, min=0, max=10):
        return cls(random.randrange(min, max), random.randrange(min, max))

    @staticmethod
    def print_parts():
        return "Cylinder is constructed using radius and height."


cylinder1 = Cylinder(2, 10)
cylinder2 = Cylinder(2, 30)

print(f"Vyska prvniho valce = {cylinder1.height} m.")
print(f"Polomer prvniho valce = {cylinder1.radius} m.")
print(f"Podstava prvniho valce = {cylinder1.base()} m2.")
print(f"Objem prvniho valce = {cylinder1.volume()} m3.")
print(f"Zakladni data o Valci 2 = {cylinder2}")

Cylinder.default_color = "blue"
print(f"Valec 1 je stejny jako Valec 2 = {cylinder1 == cylinder2}.")
print(f"Valec 1 je mensi nez Valec 2 = {cylinder1 < cylinder2}.")
print(f"Souctem obou valcu vznikne valec {cylinder1 + cylinder2}.")
print(f"Nahodny vytvoreny valec ma hodnoty {Cylinder.random_cyl()}.")
print(f"Informace ohledne valce = {Cylinder.print_parts()}")
