import random
marbles = ['зелёный','зелёный','зелёный','зелёный','зелёный','зелёный']
players = []
a = random.randint(0,5)
marbles[a] = 'белый'
print(marbles)
players_counter = int(input('сколько игроков будет играть? (макс3 и мин 2'))
while 3 < players_counter or players_counter  < 2 :
    print('много или мало игроков')
    players_counter = int(input('сколько игроков будет играть? (макс3 и мин 2)'))
    
for i in range(players_counter):
    q = input(f' Введите имя игрока #{i+1}:')
    players.append(q)
print(players)
taken = 0
current_player = 1
print('''Добро пожаловать в игру “Русская рулетка”!
Правила игры: Из меш­ка с пятью зелеными шариками и
одним белым каждый игрок по очереди достает по одному
шарику. Если достался зеленый шарик - игра идет дальше,
если кому-нибудь из игроков достался белый, то игра
заканчивается.Удачи!)''')
