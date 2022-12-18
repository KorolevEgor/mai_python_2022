from data import drone_list, drone_weight_list

# TODO4
# для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
# высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
# помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!


height = 200
directly = True
is_city = True
is_closed = False

for drone, weight in zip(drone_list,  drone_weight_list): 
    if directly and (height <= 100) and (not is_closed) and ((is_city and weight < 150) or (not is_city)):
        print('Можно не согласовывать')
    else:
        print('Нужно согласовывать')
