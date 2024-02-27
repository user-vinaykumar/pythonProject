# remove duplicates from the list.

mall = ['mantri', 'forum', 'meenakshi', 'forum', 'mantri', 'total', 'gt world']

def removeDuplicates(item):
    dupsRemoved = set(item)
    dupsRemoved = list(dupsRemoved)

    print(f'duplicates removed from the list. {dupsRemoved}')

removeDuplicates(mall)
