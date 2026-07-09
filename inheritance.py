class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
class Duck(Animal):
    def quack(self):
        print("Duck quacks")
class Lion(Animal):
    def roar(self):
        print("Lion roars")
# Creating objects
dog = Dog()
cat = Cat()
duck = Duck()
lion = Lion()

dog.eat()
dog.bark()
cat.eat()
cat.meow()
duck.eat()
duck.quack()
lion.eat()
lion.roar()