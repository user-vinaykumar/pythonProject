# to get the environment variable that is set on system.
import os
def env(item):
    value = os.environ.get(item)
    print(f'the environment variable value is : {value}')

(env('TEMP'))
(env('PATH'))