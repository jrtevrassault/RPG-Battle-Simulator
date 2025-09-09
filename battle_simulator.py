import random

class Character:
    def __init__(self, name, hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max

    def attack(self, other):
        damage = random.randint(self.attack_min, self.attack_max)
        other.hp -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        if other.hp < 0:
            other.hp = 0

    def is_alive(self):
        return self.hp > 0

def main():
    player = Character("Player", 30, 4, 8)
    enemy = Character("Enemy", 25, 3, 7)

    turn = 0
    print("Battle Start!")
    print(f"{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}\n")

    while player.is_alive() and enemy.is_alive():
        if turn % 2 == 0:
            player.attack(enemy)
        else:
            enemy.attack(player)
        print(f"{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}\n")
        turn += 1

    if player.is_alive():
        print("Player wins!")
    else:
        print("Enemy wins!")

if __name__ == "__main__":
    main()
