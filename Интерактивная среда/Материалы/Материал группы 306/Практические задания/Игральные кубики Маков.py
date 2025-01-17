import random

def dice_simulation(throws, target):
    count = 0
    for _ in range(throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 + dice2 == target:
            count += 1
    return count

# Пример использования:
throws = 1000
target = 7
result = dice_simulation(throws, target)
print(f"Сумма {target} выпала {result} раз.")