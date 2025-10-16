def count_words_ending_with_dot(text):
    if text.endswith('.'):
        words = text[:-1].split()
    else:
        words = text.split()
    return len(words)
