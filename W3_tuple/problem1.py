# convert the tuples into dictionary with x, y, z as keys given in the tuples.

sample = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

def pro(item):
    dictionary = {}
    for a, b in item:
        dictionary.setdefault(a, []).append(b)

    print(f'the tuples converted to dictionary based on key : {dictionary}')

pro(sample)
