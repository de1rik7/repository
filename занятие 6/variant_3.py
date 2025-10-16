def remove_dots(text):
    count = text.count('.')
    new_text = text.replace('.', '')
    return new_text, count