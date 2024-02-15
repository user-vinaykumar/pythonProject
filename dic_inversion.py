# here we are going to invert the key and value to one another.

dictionary = {'India' : 'Delhi',
              'Karnataka' : 'Bengaluru',
              'Tamilnadu' : 'Chennai',
              'Kerala' : 'Thiruvananthapuram',
              'Telangana' : 'Hyderabad',
              'Andhra Pradesh' : 'Vijayawada'}

new_dictionary = {city : state for state, city in dictionary.items()}

print(new_dictionary)
