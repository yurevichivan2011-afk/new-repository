# def get_middle_point(x1, y1, x2, y2):
#     x_mid = (x1 + x2) / 2
#     y_mid = (y1 + y2) / 2
#     return x_mid, y_mid
#
# print(get_middle_point(0, 0, 10, 0))
# print(get_middle_point(1, 5, 8, 3))


# def find_all(target, symbol):
#     positions = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             positions.append(i)
#     return positions
#
#
# print(find_all('abcdabcaaa', 'a'))
# print(find_all('abcadbcaaa', 'e'))
# print(find_all('abcadbcaaa', 'd'))


# def merge(list1, list2):
#     result = []
#     i, j = 0, 0
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             result.append(list1[i])
#             i += 1
#         else:
#             result.append(list2[j])
#             j += 1
#
#     while i < len(list1):
#         result.append(list1[i])
#         i += 1
#
#     while j < len(list2):
#         result.append(list2[j])
#         j += 1
#
#     return result
#
#
# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
# def get_type(value):
#  return type(value)
#
#
# print(get_type(10))
# print(get_type(3.14))
# print(get_type("Hello"))
# print(get_type([1, 2, 3]))
# print(get_type({"a": 1}))
# print(get_type(True))
# print(get_type(None))
time
random
class Resident:
    def __init__(self,name):
        self.name = name
        self.hunger = 60
        self.energy = 80
    def status(self):

class WorkerSim(Resident):
    def __init__(self, name, money):
        super().__init__(name)
    def work(self):

class LazySim(Resident)
    def __init__(self, name):
        super().laziness = 100
    def live_day(self):
        self.hunger -= 5
        self.energy -= 5
        if self.hunger <=0 or self.energy <= 0:
            self.is_alive = False
    def sleep_on_trash(self):
        print(f'{self.name} прилег на гору грязного белья.')
        self.energy += 40
        self.hunger -= 5
    def reach_to_mess(self):

worker = WorkerSim('Артур', 100)
lazy_guy = LazySim('Ларри',)
roomates = [worker, lazy_guy]

day = 1
is_messy = True

if not all(r.is_alive for r in roomates):
    dead = next(r for r in roomates if not r.is_alive)
    print(f'{dead.name} не смог смириться с камуналкой.')
    break

print(f"Общак Артура" {worker.money}$ )
for

print('\nВаш выбор:')
print('1. Артур идет на работу')
print('2. Артур купит еду на всех')
print('3. Поспать за Ларри')
print('4.Ларри просит у Артура денег')
print('5.')
print('0.')

if choise == '1'
    print()



