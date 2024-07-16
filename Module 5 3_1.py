
# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(f'args: {args}')
#         print(f'kwargs: {kwargs}')
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(f'first: {first}')
#         print(f'second: {second}')
#         print(f'thirs: {third}')
#
# ex = Example('data', second=25, third=3.14)
# print(f'ex: {ex}\ntype(ex): {type(ex)}\nex.__dict__: {ex.__dict__}')


class House:
    houses_history = [] # определяем список в классе, но до функции __new__
    def __new__(cls, *args):
        cls.houses_history.append(args[0]) # cls. является обращением к списку в классе.
        # print(f'houses_history in __new__ {cls.houses_history}') # сls здесь тоже для обращения к списку в классе
        return object.__new__(cls)
    def __init__(self, name, nof):
        self.name = name
        self.number_of_floors = nof
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return f'Название "{self.name}", количество этажей - {self.number_of_floors}.'
    def __eq__(self, other: int):
        if isinstance(other, (int, House)):
            return self.number_of_floors == other
    def __add__(self, value):
        if isinstance(value, (int, House)):
            self.number_of_floors = self.number_of_floors + value
            return self
    def __iadd__(self, value):
        if isinstance(value, (int, House)):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        if isinstance(value, (int, House)):
            self.number_of_floors += value
            return self
    def __gt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
