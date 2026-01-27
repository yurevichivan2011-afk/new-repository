# mylist = []
# mylist = list[]

# numbers = list(range(5))
# even_numbers = list(range(0, 10, 21))
# chars = list('abcde')
# print(numbers)
# print(even_numbers)
# print(chars)

 # numbers = [2, 4, 6, 8, 10]
 # languages = ('Python', 'C#', 'C++', 'Java')
 # print(len(numbers))
 # print(len(languages))
 # print(len(['apple',banana '', 'orange']))

# numbers = [2, 4, 6, 8, 10]
# if 2 in numbers:
#   print('Список numbers содержит число 2')
# else:
#  print('Список numbers не содержит число 2')

# numbers = [2, 4, 6, 8, 10]
#  if 0 not in numbers:
#    print('Список numbers не содержит 0')

# fruits = ['apple', 'banana', 'cherry', 'apricos', 'kiwi', 'lemon', 'mango']
# fruits[2] = 'orange'

# print([1, 2, 3, 4] + [5, 6, 7, 9])
# print([7,8] * 3)
# print([0] *10)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)

# numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
# print('Минимальный элемент =',min(numbers))
# print('Максимальный элемент =', max(numbers))

# numbers = [1, 2, 3, 4]
# names = ['Monica', 'Joey', 'Gunther', 'Chandler']
# print('Минимальный элемент =',min(numbers))
# print('Максимальный элемент =',max(names))

# bonks = ['1984', 'О дивный новый мир', '451 градус по фаренгайту']
# print(bonks[0][1])

# artists = ['Malevich', 'Vasnetsov','Monet']
# print(artists[0])

# numbers = [1, 2, 3, 4]
# numbers.append(21)
# numbers.append(34)
# print(numbers)

# numbers = [1, 2, 3, 4]
# odds = [5, 6, 7]
# numbers.extend(odds)
# print(numbers)

# numbers = [1, 2, 3, 4]
# del numbers[1]
# print(numbers)

# names = ['Gvido', 'Roman', 'Timur']
# position = names.index('Timur')
# print(position)

# food = ['Рис','Roman']
# item = food.pop(0)
# print(item)
# print(food)

# names = ['Gvido', 'Roman', 'Timur']
# cnt1 = names.count('Timur')
# cnt2 = names.count('Roman')
# print(cnt1)
# print(cnt2)

# names = ['Gvido', 'Roman', 'Timur']
# names. reverse()
# print(names)

# names = ['Gvido', 'Roman', 'Timur']
# names.clear()
# print(names)

# names = ['Gvido', 'Roman', 'Timur']
# names_copy = names.copy()
# print(names)
# print(names_copy)

#.sort

# prines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# print(prines[17])


# enemes = [1, 2, 3, 4, 5, 6, 7]
# average = sum(enemes) / len(enemes)
# print(enemes)

# a = int(input())
# b = []
# for i in range(a):
#     c= int(input())
#     b.append(c * c * c)
# print(b)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(len(numbers))
# print(numbers[-1]
# print(numbers[::-1])
# print('Yes' if 5 in numbers else 'no'
# print(numbers[1:-1])
# def draw_box(height, width):
#     for i in range(height):
#      print('*' * width)

# def print_texas():
#     birds = 5000
#     print('В Техасе обитает', birds, 'птиц')
#
# def print_california():
#     birds = 5000
#     print('В Какифорнии обитает', birds, 'птиц')

# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
# temp = float(input('Введите кол-во градусов по Фаренгейту:'))
# celsius = convert_to_celsius(temp)
# print(celsius)

# def compute_average(numbers):
#     numbers = [1, 2, 3, 4, 2, 6, 3, 9]
#     return sum(numbers) / len(numbers)
#     print(compute_average(numbers))

# def get_highest(names, heights):
#     max_height = max(heights)
#     index_max_height = heights.index(max_height)
#     return names[index_max_height]
# print(get_highest(['Андрей', 'Валерия', 'Елена', 'Николай', 'Жанна'], [1.75, 1.61, 1.65, 1.83, 1.64]))

# def draw_box(height):
#     for i in range(height):
#         print('*       *')
# print('***********')
# draw_box(13)
# print('*****')

# def find_all(target, symbol):
#     result = []
# print(find_all('abcadcaaa', 'e'))
#     for i in range(len(target)):
#         if target[i] == symbol:
#            result.append(i)
#     return result
# print(find_all('abcadcaaa', 'a'))
# print(find_all('abcadcaaa', 'd'))

#class car:
#    pass
# class Cat:
#     def __init__(self, name);
#     self.name = name
#     def speak(self):
#         return (self.name)
# my_cat = Cat('Kesha')
# print(my_cat_speak())
# print(my_cat)
#
# class Zombie:
# def __init__(self, name)
#     self.name = zombie
#     self.health = 50
# def grow(self):
#     return(self.name)
# z1 = Zombie
########################################E#################################
# class Character:
#        def __init__(self, name, health=100, max_health=None, damage = 20):
#               self.name = name
#               self.health = health
#               self.max_health = max_health or health
#               self.damage = damage
#
#        def status(self):
#               percent = (self.health / self.max_health) * 100
#               return f'{self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%)| Урон: {self.damage}'
#
#        def attack(self, target):
#               return f'{self.name} бьет {target.name} на {self.damage}'
#
#        def take_damage(self, damage):
#               self.health -= damage
#               if self.health < 0:
#                      self.health = 0
#               return f' {self.name} получил {damage} урона! Осталось: {self.health} HP'
#
#        def is_alive(self):
#               return self.health > 0
#
# class Enemy:
#        def __init__(self, name, health=60, damage=15):
#               self.name = name
#               self.health = health
#               self.max_health = health
#               self.damage = damage
#
#        def status(self):
#               percent = (self.health / self.max_health) * 100
#               return f'{self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%) | Урон: {self.damage}'
#
#        def attack(self, target):
#               return f'{self.name} бьет {target.name} на {self.damage}'
#
#        def take_damage(self, damage):
#               self.health -= damage
#               if self.health < 0:
#                      self.health = 0
#               return f' {self.name} получил {damage} урона! Осталось: {self.health} HP'
#
#        def is_alive(self):
#               return self.health > 0
#
# hero = Character('Люк', 120, damage=25)
# goblin = Enemy('Гоблин', 50, 12)
# boss = Enemy('Дракон', 200, 30)
#
# army = [hero, goblin, boss]
# print('Состав Армии')
# for unit in army:
#        print(unit.status())
#
# print('\n' + '=' * 50 + '\n')
#
# def battle_round(attacker, defender):
#        print(f'\n Раунд Боя:')
#        print(attacker.status())
#        print(defender.status())
#
#        print(attacker.attack(defender))
#        print(defender.take_damage(attacker.damage))
#
#        print(defender.status())
#        print('-'*30)
#
# battle_round(goblin, hero)
# battle_round(hero, goblin)
# battle_round(boss, hero)
# battle_round(hero, boss)
#
# print('\n' + '='*50 + '\n')
# print('Итоги:')
# for unit in army:
#        status = unit.status()
#        if not unit.is_alive():
#               status += 'Мертв'
#        print(status)
################################################################################


# class Home:
#        def __init__(self, name):
#               self.name = name
#
# def sleep(self, sim):
#        print(f'{sim.name} спит в доме {self.name}')
#        sim.energy += 20
#
# class Job:
#        def __init__(self, title, salary):
#               self.title = title
#               self.salary = salary
#
#        def work(self, sim):
#               print(f'{sim.name} работает как {self.title}')
#               sim.money += self.salary
#               sim.energy -= 15
#
# class Sim:
#        def __init__(self, name, home, job):
#               self.name = name
#               self.energy = 50
#               self.home = home
#               self.job = job
#
#        def eat(self):
#               print(f'{self.name} ест пищу')
#               self.energy += 10
#               self.money -= 5
#
#        def show_status(self):
#               print('----------')
#               print(f'Имя: {self.name}')
#               print(f'Энергия: {self.energy}')
#               print(f'Деньги: {self.money}')
#
# home = Home('Уютный дом')
# jop = Job('Програмист', 50)
# sim = Sim("Aleks", home, jop)
# sim.show_status()
# sim.job.work(sim)
# sim.home.sleep(sim)
# sim.eat()
# sim.show_status()
###############################################################################
import time
import random
class Sim:
       def __init__(self, name):
              self.name = name
              self.hunger = 50
              self.energy = 100
              self.is_alive = True

       def eat(self):
              if self.hunger >= 100:
                     print(f'{self.name} не хочет есть.')
              else:
                     self.hunger += 20
                     self.energy -= 5
                     print(f'{self.name} поел(а). Голод: {self.hunger}')

       def live_day(self):
              self.hunger -= 10
              self.energy -= 10
              if self.hunger <= 0 or self.energy <= 0:
                     self.is_alive = False
                     print(f'{self.name} не выержал суровой жизни и помер.')

       def status(self):
              return f'{self.name}, Голод: {self.hunger}, Энергия: {self.energy}'

class Human(Sim):
       def __init__(self, name, job):
              super().__init__(name)
              self.job = job
              self.money = 50

       def work(self):
              self.energy -= 30
              self.humger -= 20
              self.money += 100
              print(f'{self.name} сходил на работу ({self.job}). +100$. Энергия: {self.energy}')

       def feed_pet(self, pet):
              if self.money >= 20:
                     print(f'{self.name} покупает корм и кормит {pet.name}...')
                     self.money -=20
                     pet.eat()
              else:
                     print(f'у {self.name} нет денег на корм! Иди работай!!!')

       def repair_robot(self, robot):
              print(f'{self.name} чинит {robot.name}...')
              self.energy -= 20
              robot.energy = 100
              print(f'{robot.name} починен')

class Dog(Sim):
       def eat(self):
              self.hunger += 30
              print(f'{self.name} жадно грызет кость! Гав!')

       def play(self, human):
              print(f'{self.name} приносит мячик {human.name}')
              self.energy += 10
              print(f'{human.name} повеселел')

class Robot(Sim):
       def __init__(self, name):
              super().__init__(name)
              self.battery = 100

       def live_day(self):
              self.energy -= 5

       def eat(self):
              print(f'{self.name} заряжается')
              self.energy = 100

       def cook_diner(self, human):
              if self.energy > 20:
                     print(f'{self.name} готовит ужин для {human.name}.')
                     self.energy -= 20
                     human.eat()
              else:
                     print(f'{self.name} не может готовить, он разряжен')

class Cat(Sim):
       super()
       def __init__(self, lives):
              self.lives = 9
       def eat(self):
              self.humger += 30
              print(f'{self.name} ест корм. Мяу!')

       def play(self, human):
              print(f'{human.name} погладил {self.name}')
              self.energy += 10
              print(f'У {human.name} поднялось настроение')




player = Human('Алекс', 'прогромист')
doggo = Dog('Бэк')
cat = Cat('Кеша')
robo = Robot('Cook-3000')
household = [player, doggo, robo]
day = 1

print("Добро пожаловать в Sims Python Edition")

while True:
       print(f'\n=== День {day} ===')
       game_over= False
       for sim in household:
              if not sim.is_alive:
                     print(f'Проиграл: {sim.name} погиб')
                     game_over = True
       if game_over:
              break
              print(f'Деньги: {player.money}$')
              for sim in household:
       print({sim.status()})
       print('\nЧто будет делать Алекс')
       print('1. Пойти на работу')
       print('2. Поесть самому(-20$ еда)')
       print('3. Покормить Бэка и Кешу(-25$ корм)')
       print('4. Поиграть с Бэкам)')
       print('5. Попросить робота приготовить ужин')
       print('6. Починить робота')
       print('7. Поиграть с Кешей')
       print('8. Выход')
       choice = input('Твой выбор: ')

       if choice == '1':
              player.work()
       elif choice == '2':
        if player.money >= 20:
              player.money -= 20
              layer.eat()
        else:
              print('Нет денег!!! Иди работай!!!')
       elif choice == '3':
              player.feed_pet(doggo, cat)
       elif choise == '4':
              doggo.play(player)
       elif choice == '5':
              robo.cook_diner(player)
       elif choice == '6':
              player.repair_robot(robo)
       elif choice == '7':
              cat.play(player)
       elif choice == '8':
       print('Пока!')
       break
       else:
       print('Неверная команда!, день прошел в пустую...')

       print('\n Наступает ночь... Все показатели падают.')
       time.sleep(1)
       for sim in household:
       sim.live_day()














