# 35. Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.

class Point:

    def __init__(self, name, coord_x, coord_y):
        self.name = name
        self.coord_x = coord_x
        self.coord_y = coord_y
        print("New point %s with coordinates x=%d, y=%d added" % (self.name, self.coord_x, self.coord_y))





class Circle:

    def __init__(self, name, radius, coord_x, coord_y):
        self.name = name
        self.radius = radius
        self.coord_x = coord_x
        self.coord_y = coord_y
        print("New circle %s with radius=%d and coordinates x=%d, y=%d added" % (self.name, self.radius, self.coord_y, self.coord_y))

    def check(self, Point):
        import math
        x1 = self.coord_x
        y1 = self.coord_y
        r = self.radius
        x2 = Point.coord_x
        y2 = Point.coord_y
        cat1 = abs(x2 - x1)
        cat2 = abs(y2 - y1)
        gippotenuse = math.sqrt(cat1**2 + cat2**2)
        if cat1 == 0 or cat2 == 0:
            if cat1 + cat2 <= r:
                print("point is in circle1")
            else:
                print("point is not in circle1")
        elif gippotenuse <= r:
            print("point is in circle")
        else:
            print("point is not in circle2")



        print(cat1, cat2)


A = Circle("Circle A", 3, 1, 2)
b = Point("Point -2,1", -3, 2)

Circle.check(A, b)

# def fill_truck(weight_limit, box_weight):
#     qtty_of_box_loaded = weight_limit // box_weight # применено целочисленно деление
#     total_weight = 0
#     for i in range(1, qtty_of_box_loaded+1):
#         total_weight = total_weight + box_weight
#         print(("Ttl wght = %d , Ttl qtty of boxes = %d, last box weight = %d") %
#                     (total_weight, i, box_weight))
# fill_truck(2000, 500)