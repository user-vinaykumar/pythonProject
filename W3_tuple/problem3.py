# python programme to count the elements in the list until it finds the tuple.

lis = [1,3,4,5,6,7,(3,4),4,6]

def pro(item):
    count=0
    for i in item:
        if isinstance(i, tuple):
            break
        else:
            pass
        count+=1
    print(f'the tuple is at the {count}th index in the list given.')


pro(lis)