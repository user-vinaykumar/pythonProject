# stat function in OS module gives the file information.
# need to pass the file in stat() to get the info.

from datetime import datetime
import os

print(os.stat('OSstat.py')) # prints the info of the file provided inside the function.

print(os.stat('OSstat.py').st_size) # gives the info of the size of the file. in Bytes.

# like st.size - many more attribute are there

print(os.stat('OSstat.py').st_mtime)  # gives the info of the time that the file last modified.

last_mod_time = os.stat('OSstat.py').st_mtime
print(datetime.fromtimestamp(last_mod_time)) # prints the human readable time of the st_mtime


