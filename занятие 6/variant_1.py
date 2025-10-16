def count_words_starting_with_e(text):
    words = text.split()
    count = 0
    for word in words:
        if word.startswith('е') or word.startswith('Е'):
            count += 1
    return count

text = "Это пример текста, где есть слова на е и Еще одно"
print(count_words_starting_with_e(text))