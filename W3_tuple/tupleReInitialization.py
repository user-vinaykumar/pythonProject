# re-initialize tuple

sample = (1,2,3,4,5,6,7,8,9) # remove 5 and add 555

print(sample[:4] + (555, ) + sample[5:])


