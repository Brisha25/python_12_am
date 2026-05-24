def process_string(s):
    words = s.split()
    result = []
    for word in words:
        if not word:
            continue
        new_word = list(word)
        # First letter always capital
        new_word[0] = new_word[0].upper()
        for i in range(1, len(new_word)):
            prev = new_word[i-1].lower()
            curr = new_word[i].lower()
            if prev < curr:
                # Preceding occurs earlier, capital
                new_word[i] = new_word[i].upper()
            elif prev > curr:
                # Preceding occurs later, small
                new_word[i] = new_word[i].lower()
            # else: same, no change
        result.append(''.join(new_word))
    return ' '.join(result)

# Example usage
print(process_string("applE is fruit"))  # Should output: APple IS FRUiT