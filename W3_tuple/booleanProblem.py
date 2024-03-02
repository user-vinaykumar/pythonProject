# check whether the specified color present in the tuple.

sample = (('Red', 'White', 'Blue'),
          ('Green', 'Pink', 'Purple'),
          ('Orange', 'Yellow', 'Lime'))

def solution(item1, item2):
    is_color = False
    for i in item1:
        for j in i:
            if j == item2:
                print(f'the color {item2} present in the tuple.')
                break
            else:
                continue

solution(sample, 'Yellow')