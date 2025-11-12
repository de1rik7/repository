sentence = input("Введите строку: ")
words = sentence.split()
sorted_words = [''.join(sorted(word)) for word in words]
print("Результат:", ' '.join(sorted_words))