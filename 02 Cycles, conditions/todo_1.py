from data import drone_list

# TODO1
# выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество.
# учтите, что:
# 1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
# 2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

user_drones_upper = set(map(lambda x: str(x).upper(), input().split(' ')))
drone_supplier_list_upper = [drone.split(' ')[0].upper() for drone in drone_list]

for user_drone in user_drones_upper:
	if user_drone in drone_supplier_list_upper:
		if user_drone.upper() == 'DJI':
			print('DJI')
		elif user_drone.upper() == 'AUTEL':
			print('Autel')
		elif user_drone.upper() == 'PARROT':
			print('Parrot')
		elif user_drone.upper() == 'RYZE':
			print('Ryze')
		elif user_drone.upper() == 'EACHINE':
			print('Eachine')
		else:
			print('undefined')

