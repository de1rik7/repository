def words_starting_with_a_and_ending_with_ya(text):
    words = text.split()
    result = []
    for word in words:
        if word.startswith('а') or word.startswith('А'):
            result.append(word)
        elif word.endswith('я'):
            result.append(word)
    return result