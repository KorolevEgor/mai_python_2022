from data import drone_list, drone_weight_list

# TODO5*
# модифицируйте решение задания TODO1:
# теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
# например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
# производители те же: DJI, Autel, Parrot, Ryze, Eachine


user_drone_supplier = input()

for drone_model in drone_list:
    if user_drone_supplier.upper() in drone_model.upper():
        print(''.join(str(x + ' ') for x in drone_model.split(' ')[1:]))

