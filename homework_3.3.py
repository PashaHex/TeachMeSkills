STRATEGY = input('Введите стратегию для оаботы приложения(FIFO / LIFO)').upper()

with open('data.txt', 'r', encoding='utf-8') as f:
    cont = list(map(lambda x: x.strip(), f.readlines()))
    
print(cont)

while True:
    el = input('Что у вас?')
    if el:
        if el.upper() == 'LIFO':
            STRATEGY = 'LIFO'
            continue
        elif el.upper() == 'FIFO':
            STRATEGY = 'FIFO'
            continue
        elif el == 'end':
            break
        elif STRATEGY == 'LIFO':
            cont.append(el)
        elif STRATEGY == 'FIFO':
            cont.insert(0, el)        
        elif STRATEGY != 'FIFO' or SRTATEGY != 'LIFO':
            print('Введите корректный тип сортировки')
            continue
        print('Спасибо!')
    elif not cont:
        print('Примите наши извинения, но в данный момент мы ничего не можем вам предложить. Заходите позже.')
    else:
        item = cont.pop()
        print(f'Возьмите, вот вам - {item}')

cont = list(map(lambda x: x + '\n', cont))
print('Вышли из цикла', cont)

with open('data.txt', 'w', encoding='utf-8') as file:
    file.writelines(cont)