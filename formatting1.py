pi = 3.147656534

message = f'the value of pi is {pi:.2f}'
print(message)

# .2f --> rounds the value after 2 digits of decimal point
# .3f --> rounds the value after 3 digits of decimal point
message1 = f'the value of pi is {pi:.3f}'
print(message1)

message2 = 'the value of pi is {:.4f}'.format(pi)
print(message2)
