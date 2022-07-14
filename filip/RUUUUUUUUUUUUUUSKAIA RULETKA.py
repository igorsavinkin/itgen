import random
marbles = []
players = []
for i in range(6):
    marbles.append('green')
white = random.randint(0,5)
marbles[white]='white'
print(marbles)
players_counter = int(input('Введите число игроков: 2 или 3 '))
while players_counter != 2 and players_counter != 3:
    players_counter = int(input('Введите число игроков: 2 или 3 '))


for i in range(1,players_counter+1):    
    players.append( input(f'Введите имя игрока #{i}: '))
print(players)
taken = 0
current_player = 0
print('''Добро пожаловать в игру “Русская рулетка”!
    Правила игры: Из меш­ка с пятью зелеными шариками и одним белым шариком
каждый игрок по очереди достает по одному шарику.
Если достался зеленый шарик - игра идет дальше,
если кому-нибудь из игроков достался белый, то тебя убивают с пистолета
Удачи! ТАКОВА ЖИЗНЬ !!!''')
while taken != 6 :
    if current_player >= players_counter:
        current_player = 0
    u = input(f'''oчередь игрока {players[current_player]}
Нажми Enter, Чтобы достать шарик ...''')
    
        
    
    

   
    
    
