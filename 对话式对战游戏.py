# coding:utf-8
# 增加血条，敌人，攻击类型，敌人个数
import random


class Creature():
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name
        self.full_hp = hp

    def melee_attack(self):
        attack_value = random.randint(25, 35)
        return attack_value

    def magic_attack(self):
        attack_value = random.randint(0, 60)
        return attack_value

    def heal(self):
        self.hp = self.hp + random.randint(30, 50)

    def being_attack(self, attack_value):
        self.hp = self.hp - attack_value

    def not_dead(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def show_status(self):
        percent_hp = self.hp / self.full_hp
        print('{0}\'s HP '.format(self.name), end='')
        print('【' + ' ' * int((1 - percent_hp) * 20) + '#' * (int(percent_hp * 20)) + '】', end='')
        print('({0})'.format(self.hp))


player = Creature(200, 'Articuly')
enemy = Creature(80, 'Enemy')
enemy2 = Creature(120, 'Enemy2')
boss = Creature(240, 'BOSS')

while player.not_dead() and enemy.not_dead():
    player.show_status()
    enemy.show_status()
    user_input = input('Attack, Heal or Defence(A/H/D)')

    if user_input == 'A':
        player_attack_value = player.melee_attack()
        enemy_attack_value = enemy.melee_attack() * 0.9
        enemy.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'D':
        enemy_attack_value = enemy.melee_attack() * 0.1
        player.being_attack(enemy_attack_value)
    elif user_input == 'H':
        player.heal()
        enemy_attack_value = enemy.melee_attack() * 0.9
        player.being_attack(enemy_attack_value)

while player.not_dead() and enemy2.not_dead() and (not enemy.not_dead()):
    player.show_status()
    enemy2.show_status()
    user_input = input('Attack, Heal or Defence(A/H/D)')
    enemy2_choice = random.choices(['A', 'M'], weights=(0.7, 0.3))[0]
    # print(enemy2_choice)
    if user_input == 'A' and enemy2_choice == 'A':
        print('Enemy2 using melee attack.')
        player_attack_value = player.melee_attack() * 1.1
        enemy_attack_value = enemy2.melee_attack()
        enemy2.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'D' and enemy2_choice == 'A':
        print('Enemy2 using melee attack.')
        enemy_attack_value = enemy2.melee_attack() * 0.2
        player.being_attack(enemy_attack_value)
    elif user_input == 'H' and enemy2_choice == 'A':
        print('Enemy2 using melee attack.')
        player.heal()
        enemy_attack_value = enemy2.melee_attack()
        player.being_attack(enemy_attack_value)
    elif user_input == 'A' and enemy2_choice == 'M':
        print('Enemy2 using magic attack.')
        player_attack_value = player.melee_attack() * 1.1
        enemy_attack_value = enemy2.magic_attack()
        enemy2.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'D' and enemy2_choice == 'M':
        print('Enemy2 using magic attack.')
        enemy_attack_value = enemy2.magic_attack() * 0.2
        player.being_attack(enemy_attack_value)
    elif user_input == 'H' and enemy2_choice == 'M':
        print('Enemy2 using magic attack.')
        player.heal()
        enemy_attack_value = enemy2.magic_attack()
        player.being_attack(enemy_attack_value)

if player.not_dead() and (not enemy2.not_dead()) and (not enemy.not_dead()):
    print('You have upgraded and now you are facing the boss. defence is useless, but you have unlock magic attack.')

while player.not_dead() and boss.not_dead() and (not enemy2.not_dead()) and (not enemy.not_dead()):
    player.show_status()
    boss.show_status()
    user_input = input('Attack, Magic Attack or Heal(A/M/H)')
    boss_choice = random.choices(['A', 'M'], weights=(0.6, 0.4))[0]
    # print(boss_choice)
    if user_input == 'A' and boss_choice == 'A':
        print('Boss using melee attack.')
        player_attack_value = player.melee_attack() * 1.2
        enemy_attack_value = boss.melee_attack() * 1.1
        boss.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'M' and boss_choice == 'A':
        print('Boss using melee attack.')
        player_attack_value = player.magic_attack() * 1.3
        enemy_attack_value = boss.melee_attack() * 1.1
        boss.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'H' and boss_choice == 'A':
        print('Boss using melee attack.')
        player.heal()
        enemy_attack_value = boss.melee_attack()
        player.being_attack(enemy_attack_value)
    elif user_input == 'A' and boss_choice == 'M':
        print('Boss using magic attack.')
        player_attack_value = player.melee_attack() * 1.2
        enemy_attack_value = boss.magic_attack() * 1.1
        boss.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'M' and boss_choice == 'M':
        print('Boss using magic attack.')
        player_attack_value = player.magic_attack() * 1.3
        enemy_attack_value = boss.magic_attack() * 1.1
        boss.being_attack(player_attack_value)
        player.being_attack(enemy_attack_value)
    elif user_input == 'H' and boss_choice == 'M':
        print('Boss using magic attack.')
        player.heal()
        enemy_attack_value = boss.magic_attack() * 1.1
        player.being_attack(enemy_attack_value)

if player.not_dead():
    print('You win!')
else:
    print('You lose!')
