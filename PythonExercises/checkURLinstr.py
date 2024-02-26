# check whether the string contains any URL in it.

import re

url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"


str = 'I work at https://www.youtube.com/watch?v=Nk-CJcDZkAc&list=PLUDwpEzHYYLv0iZsTx4dm-v-icoVXRqrz&index=25 and https://www.bing.com/search?pglt=2209&q=github+login&cvid=5d5209e1f5eb427b93cd584e2ec479be&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEEUYPDIGCAcQRRg8MgYICBBFGDzSAQkyNDE3NWowajGoAgCwAgA&FORM=ANSPA1&PC=U531&ntref=1'

url = re.findall('"^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"', str)

print(url)
