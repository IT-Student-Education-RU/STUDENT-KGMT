class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def __init__(self, name, age, breed, favorite_toy):
        super().__init__(name, age, breed)
        self.favorite_toy = favorite_toy

    def info(self):
        return f"{super().info()}, Favorite Toy: {self.favorite_toy}"

    def make_sound(self):
        return "Woof!"

    def bring_ball(self):
        return f"{self.name} играет в мяч!"


class Cat(Animal):
    def __init__(self, name, age, breed, favorite_food):
        super().__init__(name, age, breed)
        self.favorite_food = favorite_food

    def info(self):
        return f"{super().info()}, Favorite Food: {self.favorite_food}"

    def make_sound(self):
        return "Meow!"

    def catching_mice(self):
        return f"{self.name} ловит мышей"
dog = Dog("Buddy", 3, "Golden Retriever", "Ball")
cat = Cat("Whiskers", 2, "Siamese", "Tuna")

print(dog.info())
print(dog.make_sound())
print(dog.bring_ball())

print(cat.info())
print(cat.make_sound())
print(cat.catching_mice())
