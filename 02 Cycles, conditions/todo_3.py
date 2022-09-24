from data import drone_list, drone_weight_list

# TODO3
# выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество.
# сделайте то же самое для всех дронов, которые не нужно регистрировать
# для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
# как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

register_count = 0
not_register_count = 0
for drone, weight in zip(drone_list,  drone_weight_list):
    if weight > 150:
        register_count += 1
        print(drone, weight)
    else:
        not_register_count += 1
print('register_count = ' + str(register_count))
print('not_register_count = ' + str(not_register_count))



