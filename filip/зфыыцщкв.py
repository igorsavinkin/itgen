
while True :
    p1 = input('введите пароль ')
    print('повторите пароль ')
    p2 = input('введите пароль ')
    if p1 != p2 :
        print("различный пароль")
        print('придумайте новый  пароль ')

        print('повторите пароль ')
        continue
    elif "123"in p1:
        print("Лёгкий пароль")
        print('придумайте новый  пароль ')

        print('повторите пароль ')
        continue
    elif"password" in p1:
        print("Лёгкий пароль")
        print('придумайте новый  пароль ')

        print('повторите пароль ')
        continue
    elif len(p1) <=8:
        print("короткий пароль")
        print('придумайте новый  пароль ')
        print('повторите пароль ')
        continue
    else:
        print('Надёжный пароль ЗАПОМНИТЕ ЕГО')
        break
        
    
        
        
        
    
