def count_lettet_t_loop(text):
    count = 0
    for char in text.lower():
        if char == 'т':
            count += 1
    return count