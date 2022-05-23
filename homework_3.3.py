import json

STRATEGY = input('Введите стратегию для оаботы приложения(FIFO / LIFO)').upper()

with open('data.txt', 'r') as f:
    cont = json.load(f)   

print(cont)
row_dict = {}
while True:
    el = input('Что у вас?')    
    if el:
        if el == 'end':
            break
        #num = int(input('Сколько ?'))
        #row_dict = {'name': el, 'amount': num}
        elif el.upper() == 'LIFO':
            STRATEGY = 'LIFO'
            continue
        elif el.upper() == 'FIFO':
            STRATEGY = 'FIFO'
            continue        
        else:
            num = int(input('Сколько ?'))
            row_dict = {'name': el, 'amount': num}        
            if STRATEGY == 'LIFO':            
                cont.append(row_dict)
            elif STRATEGY == 'FIFO':            
                cont.insert(0, row_dict)        
            elif STRATEGY != 'FIFO' or SRTATEGY != 'LIFO':
                print('Введите корректный тип сортировки')
                continue
        print('Спасибо!')
    elif not cont:
        print('Примите наши извинения, но в данный момент мы ничего не можем вам предложить. Заходите позже.')
    else:
        item = cont.pop()
        print(f"озьмите, вот вам - {item['name']} {item['amount']} (шт)")

print('Вышли из цикла', cont)        

with open('data.txt', 'w') as file:
    json.dump(cont, file)