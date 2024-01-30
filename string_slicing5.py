str = input('Enter the string : ')

str2 = ''

                                    # Vinay kumar g s
                                    # vInay kumar g s
                                    # viNay kumar g s
                                    # vinAy kumar g s
                                    # vinaY kumar g s
                                    # vinay Kumar g s
                                    # vinay kUmar g s
                                    # vinay kuMar g s
L = str.split()
h =0

for a in L:
    print(len(L[h]))
    h += 1



'''for i in L:
    j = 0
    b = 0
    if(j>0):
        for y in range(len(i)):
            str2 = ""
            if (y == 0):
                str2 = str[:len(L[j-1]) + b ] + i[y].upper() + str[y + 1:]
                print(str2)

            else:
                str2 = str[0:y] + i[y].upper() + str[y + 1:]
                print(str2)
            b += 1


    else:
        for k in range(len(i)):
            if (k == 0):
                str2 = str2 + i[k].upper() + str[k + 1:]
                print(str2)

            else:
                str2 = str[0:k] + i[k].upper() + str[k + 1:]
                print(str2)



    print(" ")
    j += 1'''

