# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# my_favorite_songs_dict = {
#     'Waste a Moment': 3.03,
#     'New Salvation': 4.02,
#     'Staying\' Alive': 3.40,
#     'Out of Touch': 3.03,
#     'A Sorta Fairytale': 5.28,
#     'Easy': 4.15,
#     'Beautiful Day': 4.04,
#     'Nowhere to Run': 2.58,
#     'In This World': 4.02,
# }

from random import sample

my_favorite_songs_dict = {
   'Waste a Moment': 3.03,
   'New Salvation': 4.02,
   'Staying\' Alive': 3.40,
   'Out of Touch': 3.03,
   'A Sorta Fairytale': 5.28,
   'Easy': 4.15,
   'Beautiful Day': 4.04,
   'Nowhere to Run': 2.58,
   'In This World': 4.02,
}

random_songs = sample(list(my_favorite_songs_dict.values()), 3)
print(random_songs)
duration = 0
for song in random_songs:
    duration = duration + song

print(f'Три песни звучат {int(duration)} минут')
