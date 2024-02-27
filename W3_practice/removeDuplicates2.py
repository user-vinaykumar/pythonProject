# remove duplicates second approach

area = ['banashankari', 'jayanagara', 'bellandooru', 'mahadevapura', 'jayanagara', 'banashankari']


def removeDuplicates(item):
    new = []
    for i in item:
        if i not in new:
            new.append(i)
        else:
            continue

    print(f'the duplicates removed and stored here : {new}')

removeDuplicates(area)