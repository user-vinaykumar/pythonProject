# simulate the traffic light

import time

light = [('Green', 2), ('Red', 2), ('Yellow', 1)]



#count = 1

def traffic_light_simulator():
    i = 0
    while True:
        length = len(light)
        c, t = light[i]
        print(c)
        time.sleep(t)
        if i == length-1:
            i = 0
        else:
            i+=1
    #if count == 6:
     #   break

   # else:
    #    count+=1

traffic_light_simulator()
