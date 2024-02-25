# remove the nth ocurrence of a given word.

lis = ['geeks', 'for', 'geeks']

new = []

for i in lis:
    if i not in new:
        new.append(i)
    else:
        pass
print(new)


