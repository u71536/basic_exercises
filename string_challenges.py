# Вывести последнюю букву в слове
print('Задание 1')
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print(f'\nЗадание 2')
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
print(f'\nЗадание 3')
word = 'Архангельск'
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
vowels_sum = sum(1 for letter in word if letter in vowels)
print(vowels_sum)


# Вывести количество слов в предложении
print(f'\nЗадание 4')
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
print(f'\nЗадание 5')
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])

# Вывести усреднённую длину слова в предложении
print(f'\nЗадание 6')
sentence = 'Мы приехали в гости'
words = sentence.split()
avg_word = sum(len(word) for word in words) / len(words)
print(avg_word)
