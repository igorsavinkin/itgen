import random
marbles = []
players = []
marbeles_counter = int(input('Введите число шариков : '))
for i in range(marbeles_counter):
    marbles.append('green')
white = random.randint(0, marbeles_counter-1)
marbles[white]='white'

players_counter = int(input('Введите число игроков : '))
while  players_counter > marbeles_counter // 2 or  players_counter < 2:
    players_counter = int(input('Введите заново число игроков :  '))
    

for i in range(1,players_counter+1):    
    players.append( input(f'Введите имя игрока #{i}: '))
print(players)
taken = 0
current_player = 0

    
#print(marbles)

print('''Добро пожаловать в игру “Русская рулетка”!
Правила игры: Из мешка с N зелеными шариками и одним белым шариком
каждый игрок по очереди достает по одному шарику.
Если достался зеленый шарик - игра идет дальше и шарик возвращается в мешок.
Если кому-нибудь из игроков достался белый, то он проиграл.''')
while taken != marbeles_counter :
    if current_player >= players_counter:
        current_player = 0
    u = input(f'''Очередь игрока {players[current_player]}
    Нажмите "Enter" чтобы снова достать шарик.''')
    chosen_marble = random.choice(marbles)
    if chosen_marble == 'white':
        print('Игрок достал белый шарик')
        print(f'''Игрок под именем {players[current_player]} уже труп СКОРО НАМЕЧАЮТСЯ ПОХОРОНЫ''')
        break
    else:
        print('Всё хорошо, Вам попался зелёный шарик.')
        print('Ход переходит к следушему игроку.')
        current_player +=1
        random.shuffle(marbles)  
        
    
    

   
    
    
