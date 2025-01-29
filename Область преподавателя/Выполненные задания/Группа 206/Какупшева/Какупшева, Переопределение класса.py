class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

    def bring_ball(self):
        return "Собака принесла мяч!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

    def catching_nice(self):
        return "Кошка ловит мышку!"
