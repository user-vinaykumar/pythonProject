# open the youtube by python code.

import webbrowser
import time



def authentication():
    userName = input('Enter the userName : ')
    passWord = input('Enter the password : ')
    if passWord == '12345678;':
        return True
    else:
        return False


def openBrowser(item):
    if authentication() == True:
        time.sleep(2.0)
        print(f'loading....Wait...')
        webbrowser.open(item)
    else:
        time.sleep(2.0)
        print(f'loading.....Wait...')
        time.sleep(5.0)
        print(f'The password you entered is Wrong...!!!')
        print(f'Could not open the browser....')


openBrowser("https://www.youtube.com")