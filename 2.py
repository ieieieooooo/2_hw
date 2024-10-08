
class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage):
        self.health -= max(damage - self.armor, 0)

    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def current_health(self):
        return self.health


class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Battle:

    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        while player.current_health() > 0 and enemy.current_health() > 0:
            if player.attack(enemy):
                print(f"Игрок атаковал и нанес {enemy.current_health()} урона врагу.")
            elif enemy.attack(player):
                print(f"Враг атаковал и нанес {player.current_health()} урона игроку.")
            else:
                break

        if player.current_health() <= 0:
            print("Игрок умер :(")
        elif enemy.current_health() <= 0:
            print("Враг умер!")
        else:
            print("Ничья")

if __name__ == "__main__":

    player = Player('Алеша', 1000, 770, 10)
    enemy = Enemy('Чипс', 95, 21, 8)
    battle = Battle(player, enemy)

    battle.start()