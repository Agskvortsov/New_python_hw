# 36. Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.
# В родительском классе должно быть определено минимум 1 инициализатор, 3 атрибута и 1 метод.
# В классах-потомках должны быть добавлены минимум по 1 новому методу и по 1 новому атрибуту.

class Transport:

    def __init__(self, name="", max_pass_cap=0, max_cargo_cap=0, speed=0):
        self.name = name
        self.max_pass_cap = max_pass_cap
        self.max_cargo_cap = max_cargo_cap
        self.acctual_cargo_cap = 0
        self.acctual_pass_cap = 0
        self.speed = speed

    def loading_of_transport(self, num_of_pass, qtty_of_cargo):
        self.acctual_pass_cap = self.acctual_pass_cap + num_of_pass
        self.acctual_cargo_cap = self.acctual_cargo_cap + qtty_of_cargo
        self.print_info()
        print("Loaded %d passangers and %d tons of cargo" % (num_of_pass, qtty_of_cargo))
        print("------------------------------------------------")



    def print_info(self):
        print("=========================")
        print("Name -", self.name)
        print("Max passanger qtty -", self.max_pass_cap)
        print("Max cargo qtty -", self.max_cargo_cap)
        print("Acctual pass on board -", self.acctual_pass_cap)
        print("Acctual cargo qtty -", self.acctual_cargo_cap)
        print("Speed -", self.speed)
        print("------------------------------------------------")


    def estim_trip_time(self, distance):
        self.speed_when_laden = self.speed - self.speed * 0.2 * ((self.acctual_cargo_cap + self.acctual_pass_cap) /
                                                                 (self.max_cargo_cap + self.max_pass_cap))
        self.print_info()
        print("Estimated time for trip is - %s hours" % (distance / self.speed_when_laden) )
        print("Current condition speed -", self.speed - self.speed * 0.2 * ((self.acctual_cargo_cap + self.acctual_pass_cap) /
                                                                (self.max_cargo_cap + self.max_pass_cap)))
        print("------------------------------------------------")




class Train(Transport):
    max_qtty_of_wagons = 10
    def __init__(self, wor):
        Transport.__init__(self)
        self.wor = wor
        self.redinace_for_voyage = "No"

    def checkin_before_departure(self, qtty_of_wags, actual_wor):
        if self.max_qtty_of_wagons >= qtty_of_wags and self.wor == actual_wor:
            self.redinace_for_voyage = "Yes"
            print("Traine is ready for voyage")
        elif self.max_qtty_of_wagons <qtty_of_wags:
            self.redinace_for_voyage = "No"
            print("reduce qtty of vagons to", self.max_qtty_of_wagons)
        else:
            self.redinace_for_voyage = "No"
            print("check wor")



 # def __init__(self):
 #          Figura.__init__(self)
 #          self.radius=55
 #          self.tl=2
 #          self.form='oval'






train1 = Transport("TuTu1", 600, 2000, 150)
train2 = Train(122)
print(train1.max_cargo_cap)
print(train2.redinace_for_voyage)
train2.checkin_before_departure(11, 122)
# train2.max_cargo_cap = 150
# train2.print_info()
# print(train2.max_qtty_of_wagons)
# checkin_before_departure.Train

# #
# train1.print_info()
# train1.estim_trip_time(600)
# train1.loading_of_transport(44 , 190)
# train1.estim_trip_time(600)
# train1.loading_of_transport(0 , 600)
# train1.estim_trip_time(600)