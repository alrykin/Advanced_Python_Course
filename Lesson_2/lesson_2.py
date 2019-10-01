
########################################
################ Задача 1
class Vehicle:

    def __init__(self, color=None, doors=4, brand=None, ):
        self.doors = doors
        self.color = color
        self.brand = brand

    def purpose(self):
        return "purpose of Vehicle depends..."
    def carrying_capacity(self, weight):
        return weight >= 100


class Car(Vehicle):
    def purpose(self):
        return "transport or just for fun"



class Truck(Vehicle):
    def purpose(self):
        return "for transportation of goods"
    def carrying_capacity(self, weight):
        return weight >= 500


MyCar = Truck(brand = 'KRAZ')
print(MyCar.purpose())
print(MyCar.carrying_capacity(600))


########################################3
################ Задача 2

class EStore:
    ALL_STORES_SOLD = 0
    def __init__(self, title, sold_goods=0):
        self._sold_goods = sold_goods
        self._title = title

    def sold(self,  num = 1):
        self._sold_goods = self._sold_goods + num
        EStore.ALL_STORES_SOLD = EStore.ALL_STORES_SOLD + num

    def print_all_stores_sold(self):
        print("All stores sold count: " + str(EStore.ALL_STORES_SOLD))



print("~~~~~~  rozetka  ~~~~~~~~")
estore_rozetka = EStore("Rozetka.ua", 0)
estore_rozetka.sold(2)
print(estore_rozetka._sold_goods)
estore_rozetka.print_all_stores_sold()


print("~~~~~~  hotline  ~~~~~~~~")
estore_hotline = EStore("Hotline.ua", 0)
estore_hotline.sold(3)
print(estore_hotline._sold_goods)
estore_hotline.print_all_stores_sold()


print("~~~~~~  prom  ~~~~~~~~")
estore_prom = EStore("prom.ua", 0)
estore_prom.print_all_stores_sold()


########################################3
################ Задача 3
class Coordinats:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        print(self.x)

    def get_y(self):
        print(self.y)

    def get_z(self):
        print(self.z)

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y

    def set_z(self,z):
        self.z = z

    def __mul__(self, other):
        print(self.x * other.x, self.y * other.y, self.z * other.z)


coord = Coordinats(1,2,3)
coord.set_x(1)
coord.get_x()
coord2 =  Coordinats(1,2,3)

coord * coord2
