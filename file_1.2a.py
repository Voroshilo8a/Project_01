# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# my_favorite_songs = [
#     ['Waste a Moment', 3.03],
#     ['New Salvation', 4.02],
#     ['Staying\' Alive', 3.40],
#     ['Out of Touch', 3.03],
#     ['A Sorta Fairytale', 5.28],
#     ['Easy', 4.15],
#     ['Beautiful Day', 4.04],
#     ['Nowhere to Run', 2.58],
#     ['In This World', 4.02],

for random import sample

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

list_of_songs = sample(my_favorite_songs, 3)
print(list_of_songs)

duration = 0
for song in list_of_songs:
    duration = duration + song[1]

print(f'Три песни звучат {int(duration)} минут')