# Напишите ваше решение
speed = int(input("введите скорость"))
time_ = int(input("введите время скачивания"))
coast = int(input("введите стоимость Гб"))

game_gbytes = (time_ * 60 * speed) / 1024 / 1024

oplata = (game_gbytes - 1) * coast
print(game_gbytes)

print(oplata)
