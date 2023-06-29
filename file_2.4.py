# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"



s = input('Введите текст  ')

def remove_last_em(s):
    text = s.replace('!','')
    return text

print(remove_last_em(s))