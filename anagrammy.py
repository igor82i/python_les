# Анаrраммы CWord JumЬle)
#
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово
import random

#создадим последовательность слов. из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)

correct = word

jumble = ''
score = 0
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("""
Добро пожаловать в игру Анаграммы!

""")
print('Вот анаграмма: ', jumble)
var1 = input('Вам нужна подсказка Да или Нет: ',)
if var1 == 'да':
    print('Подсказка: ')
    score +=3
    if correct == 'питон':
        print('Присмыкаемое')
    elif correct == "анаграмма":
        print('Название программы')
    elif correct == "простая":
        print('простая')
    elif correct == "сложная":
        print('сложная')
    elif correct == "ответ":
        print('противоположность вопросу')
    elif correct == "подстаканник":
        print('В машине')
else:
    score +=5

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print('Не верно')
    guess = input("Попробуйте отгадать исходное слово: ")
    score -=1
if guess == correct:
    print("Дa. именно так! Вы отгадали!\n")
print("Cnacибo за игру.", 'Ващ счёт равен: ', score)
input("\n\nHaжмитe Enter. чтобы выйти.")