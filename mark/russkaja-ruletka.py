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
current_player = 0
print('''Добро пожаловать в игру “Русская рулетка”!
Правила игры: Из меш­ка с пятью зелеными шариками и
одним белым каждый игрок по очереди достает по одному
шарику. Если достался зеленый шарик - игра идет дальше,
если кому-нибудь из игроков достался белый, то игра
заканчивается.Удачи!)''')
while taken < 6:
    if current_player > players_counter - 1:
        current_player = 0
    print(f'очередь игрока {players[current_player]} ')
    input('Нажми Enter, чтобы достать шарик...')
    chosen_marble = random.choice(marbles)
    marbles.remove(chosen_marble)
    if chosen_marble == 'белый':
        print('белый шарик!')
        print('выстрел в голову в', players[current_player] ,'с базуки он проигра конец игры')
        break
    elif chosen_marble == 'зелёный':
        print('жив (не труп)')
    current_player += 1
    taken += 1
print('конец игры')
        
