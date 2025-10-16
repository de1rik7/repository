def longest_sequence_of_n_and_replace_exclamation(text):
    max_n_seq = max(len(seq) for seq in text.split('н') if seq == 'н' * len(seq))
    new_text = text.replace('!', '.')
    return max_n_seq, new_text