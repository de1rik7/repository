def words_ending_with_ya(text):
    words = text.split()
    return [word for word in words if word.endswith('я')]