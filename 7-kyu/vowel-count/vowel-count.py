def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for d in sentence:
        if d in vowels:
            count += 1
    return count