def text_inside_brackets(text):
    start = text.find('(')
    end = text.find(')')
    if start != -1 and end != -1 and start < end:
        return text[start+1:end]
    return ''