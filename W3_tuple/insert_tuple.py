# insert an item into tuple

cities = ('mandya', 'mysuru', 'bengaluru', 'tumakuru', 'chamarajanagara')

lis = list(cities)
lis.append('hassana')
cities = tuple(lis)

print(cities)