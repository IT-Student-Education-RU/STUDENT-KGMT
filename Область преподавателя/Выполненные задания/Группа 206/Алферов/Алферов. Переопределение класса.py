class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def bring_ball(self):
        print("The dog is bringing the ball")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def catch_mice(self):
        print("The cat is catching mice")

dog = Dog()
dog.make_sound()
dog.bring_ball()

cat = Cat()
cat.make_sound()
cat.catch_mice()