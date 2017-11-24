# car_speed = input("Input car speed")
# distance_to_observer = input("Input distance to observer")
# angle_of_observer = input("Input angle of observer")

car_speed = 100
distance_to_observer = 300
angle_of_observer = 20




import math

def gippo_length(cat1, angle):
    angle_A = float(angle)
    angle_C = 90
    angle_B = 180 - angle_C - angle_A
    g = cat1 * math.sin(math.radians(angle_C))/math.sin(math.radians(angle_B))
    cat2 = cat1 * math.sin(math.radians(angle_A))/math.sin(math.radians(angle_B))
    g2 = math.sqrt((cat1-car_speed/3600)**2 + cat2**2)
    diff_speed = (g - g2)*3600
    print(diff_speed)







gippo_length(distance_to_observer, angle_of_observer)


