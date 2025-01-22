import math

def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


x1 = float(input("Введите x1: "))
y1 = float(input("Введите  y1: "))
x2 = float(input("Введите  x2: "))
y2 = float(input("Введите  y2: "))


dist = calculate_distance(x1, y1, x2, y2)


print(f"Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно {dist:.2f}")


def find_roots(a, b, c):

    d = math.pow(b, 2) - 4 * a * c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2
    elif d == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None



a = float(input("Введите  a: "))
b = float(input("Введите  b: "))
c = float(input("Введите c: "))


if a == 0:
    print("Коэффициент a не может быть равен нулю.не квадратное уравнение.")
else:
    roots = find_roots(a, b, c)


    if roots is None:
        print("Уравнение не имеет корней.")
    elif len(roots) == 1:
        print(f"Уравнение имеет один корень: x = {roots[0]:.2f}")
    else:
        print(f"Уравнение имеет два корня: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")


def calculate(radius):
    circum = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circum, area


r = float(input("Введите радиус : "))


if r < 0:
    print("Радиус не может быть отрицательным.")
else:
    circum, area = calculate(r)
    print(f"Длина окружности: {circum:.2f}")
    print(f"Площадь круга: {area:.2f}")