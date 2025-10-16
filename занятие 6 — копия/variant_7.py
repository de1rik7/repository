def replace_p_in_first_half(text):
    n = len(text)
    half = n // 2
    first_half = text[:half]
    second_half = text[half:]
    new_first_half = first_half.replace('п', '*').replace('П', '*')
    return new_first_half + second_half
