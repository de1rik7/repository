def remove_letter_a(text):
    count = text.count('а')
    new_text = text.replace('а', '')
    return new_text, count