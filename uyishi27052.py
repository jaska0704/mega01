def mega(dictionary):
    values = list(dictionary.values())
    for i in range(0, len(values), 2):
        if i < len(values) - 1:
            values[i], values[i+1] = values[i+1], values[i]
    mana_dict = dict(zip(dictionary.keys(), values))
    return mana_dict
print(mega({'Apple': 5, 'Banana': 2, 'Cherry': 7, 'Date': 8, 'Elderberry': 12}))
