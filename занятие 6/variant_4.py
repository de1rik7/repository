def replace_a_with_o(text):
    count = text.count('а')
    new_text = text.replace('а', 'о')
    total_chars = len(text)
    return new_text, count, total_chars