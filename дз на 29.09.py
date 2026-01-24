#Моя концепция игры: это простая игра про боевку гладиаторов. В будущем хочется создать хорошую игру проних.
#Здесь проихходит бой гладиатора Макса и Цезаря.




import random


class Gladiator:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, opponent):
        damage_dealt = max(0, self.attack_power - opponent.defense)
        opponent.health -= damage_dealt
        return damage_dealt

    def is_alive(self):
        return self.health > 0

    def status(self):
        return f"{self.name}: Health={self.health}, Attack Power={self.attack_power}, Defense={self.defense}"


class Arena:
    def __init__(self, name):
        self.name = name

    def start_fight(self, gladiator1, gladiator2):
        print(f"Бой на арене '{self.name}' между {gladiator1.name} и {gladiator2.name} начался!")

        while gladiator1.is_alive() and gladiator2.is_alive():
            damage = gladiator1.attack(gladiator2)
            print(f"{gladiator1.name} атакует {gladiator2.name} и наносит {damage} урона!")
            print(gladiator2.status())

            if not gladiator2.is_alive():
                print(f"{gladiator2.name} пал в бою!")
                break

            damage = gladiator2.attack(gladiator1)
            print(f"{gladiator2.name} атакует {gladiator1.name} и наносит {damage} урона!")
            print(gladiator1.status())

            if not gladiator1.is_alive():
                print(f"{gladiator1.name} пал в бою!")


def main():
    # Создаём гладиаторов
    gladiator1 = Gladiator(name="Макс", health=100, attack_power=20, defense=5)
    gladiator2 = Gladiator(name="Цезарь", health=100, attack_power=15, defense=10)

    # Создаём арену
    arena = Arena(name="Арена Колизея")

    # Начинаем бой
    arena.start_fight(gladiator1, gladiator2)


if __name__ == "__main__":
    main()
