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
if players != 2:
    marbles.remove('green')
    marbles.append('blue')
    
#print(marbles)

print('''Добро пожаловать в игру “Русская рулетка”!
    Правила игры: Из меш­ка с пятью зелеными шариками и одним белым шариком
каждый игрок по очереди достает по одному шарику.
Если достался зеленый шарик - игра идет дальше,
если кому-нибудь из игроков достался белый, то тебя убивают с пистолета
Удачи! ТАКОВА ЖИЗНЬ !!!''')
while taken != marbeles_counter :
    if current_player >= players_counter:
        current_player = 0
    u = input(f'''oчередь игрока {players[current_player]}
Нажми Enter, Чтобы достать шарик ...''')
    chosen_marble = random.choice(marbles)
    marbles.remove(chosen_marble)
    if chosen_marble == 'white':
        print('Игрок достал белый шарик')
        print(f'''Игрок под именем {players[current_player]} уже труп СКОРО НАМЕЧАЮТСЯ ПОХОРОНЫ''')
        break
    elif chosen_marble == 'blue':
        print(f'''Попался синий шарик
игрок { players[current_player]} выбывает''')
        players.remove(players[current_player])
        players_counter -= 1
    else:
        print('Всё хорошо, Вам попался зелёный шарик.')
        print('Ход переходит к следушему игроку.')
        taken += 1
        current_player +=1
    
        
    
    

   
    
    
