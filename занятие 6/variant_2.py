def replace_colons_with_percent(text):
    count = text.count(';')
    new_text = text.replace(';', '%')
    return new_text, count
