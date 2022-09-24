from data import drone_list

# TODO2
# подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

count = {'DJI': 0, 'AUTEL': 0, 'PARROT': 0, 'RYZE': 0, 'EACHINE': 0}

for model in drone_list:
    supplier = model.split(' ')[0].upper()
    if supplier in list(count.keys()):
        count[supplier] += 1

print(count)
