from data import drone_list, drone_weight_list

# TODO4
# для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
# высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
# помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!


height = 110
above = True
outside_of_closed_areas = False
direct_see = True

for drone, weight in zip(drone_list,  drone_weight_list):
    if (weight > 150 and above) or (height <= 100 and above and not outside_of_closed_areas and not direct_see):
        print('Нужно согласовывать')
    else:
        print('Можно не согласовывать')

