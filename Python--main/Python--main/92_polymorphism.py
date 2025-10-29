

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
# Demonstrating polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")