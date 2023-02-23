import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        self.hp -= amount

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            print(f"{self.name} hits {enemy.name} for {damage} damage!")
            enemy.take_damage(damage)
        else:
            print(f"{self.name}'s attack bounces off {enemy.name}'s defenses!")

class Player(Character):
    def move(self, direction):
        if direction == "north":
            print(f"{self.name} moves north.")
        elif direction == "south":
            print(f"{self.name} moves south.")
        elif direction == "east":
            print(f"{self.name} moves east.")
        elif direction == "west":
            print(f"{self.name} moves west.")

class Enemy(Character):
    def __init__(self, name, hp, attack, defense, xp):
        super().__init__(name, hp, attack, defense)
        self.xp = xp

    def defeated(self):
        print(f"{self.name} has been defeated!")
        return self.xp

class Game:
    def __init__(self):
        self.player = Player("Player", 100, 10, 5)
        self.enemies = [
            Enemy("Goblin", 50, 5, 2, 10),
            Enemy("Skeleton", 75, 8, 4, 20),
            Enemy("Orc", 100, 12, 6, 30)
        ]
        self.current_enemy = None

    def start(self):
        print("Welcome to the game!")
        self.player.move("north")
        self.current_enemy = self.generate_enemy()
        self.battle()

    def generate_enemy(self):
        return random.choice(self.enemies)

    def battle(self):
        print(f"You encounter a {self.current_enemy.name}!")
        while self.current_enemy.hp > 0 and self.player.hp > 0:
            action = input("What will you do? (attack/run)")
            if action == "attack":
                self.player.attack_enemy(self.current_enemy)
                if self.current_enemy.hp > 0:
                    self.current_enemy.attack_enemy(self.player)
            elif action == "run":
                if random.randint(1, 2) == 1:
                    print("You successfully run away.")
                    return
                else:
                    print("You failed to run away.")
                    self.current_enemy.attack_enemy(self.player)
            else:
                print("Invalid input.")
        if self.current_enemy.hp <= 0:
            xp = self.current_enemy.defeated()
            self.player.hp += xp
            self.current_enemy = self.generate_enemy()
            self.battle()
        elif self.player.hp <= 0:
            print("You have been defeated.")

game = Game()
game.start()
