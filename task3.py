class Buiding:  # Создайте новый класс
    def __init__(self):  # инициализатор для класса Buiding
        self.numberOfFloors = 10  # целочисленный атрибут этажности self.numberOfFloors
        self.buildingType = 'Десятиэтажка'  # строковый атрибут self.buildingType

    def __eg__(self):
        return self.numberOfFloors and self.buildingType


floors = Buiding()
building_ = Buiding()
floors.numberOfFloors = 10
building_.buildingType = 'Десятиэтажка'

if floors.numberOfFloors == building_.buildingType:  # используйте атрибут numberOfFloors и buildingType для сравнения
    print('равны')
else:
    print('нельзя сравнивать')
