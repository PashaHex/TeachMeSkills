STRATEGY = input('Введите стратегию для оаботы приложения(FIFO / LIFO)')

cont = []
while True:
    el = input('Что у вас?')
    if el:
        if STRATEGY.upper() == 'LIFO':
            cont.append(el)
        elif STRATEGY.upper() == 'FIFO':
            cont.inser(0, el)
        else:
            print('Введите корректный тип сортировки')
        print('Спасибо!')
    elif not cont:
        print('Примите наши извинения, но в данный момент мы ничего не можем вам предложить. Заходите позже.')
    else:
        item = cont.pop()
        print(f'Возьмите, вот вам {item}')