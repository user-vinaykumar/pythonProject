# reset password of the user to new password.
import time


def newPassword():
    newpwd = (input('Enter the new Password : '))
    return newpwd

def resetPassword(item):
    passwordList = list(item)
    passwordList.clear()
    passwordList.append(newPassword())
    if len(passwordList) == 1:
        time.sleep(4.0)
        print(f'the new password saved successfully!!!')
    else:
        pass

    return passwordList

def changePassword():
    oldPassword = tuple(input('Enter the old password : '))
    resetPassword(oldPassword)

changePassword()




