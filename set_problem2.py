# describe who likes what.

likes_plants = {6, 12, 15, 18, 23, 24}
likes_ecology = {1, 4, 5, 10, 15, 18, 19, 20, 21, 25}
likes_genetics = {3, 4, 6, 19, 22}

# people who only likes genetics


print("People who likes only genetics : ", likes_genetics.difference(likes_plants, likes_ecology))

# people who likes all of them

print('People who likes all of them : ', likes_ecology.intersection(likes_plants, likes_genetics))

