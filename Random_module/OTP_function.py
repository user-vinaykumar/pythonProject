import random
import time


def timer():
    time.sleep(3.0)


userCredentials = {'sajsjd': 'fsjfjd',
                   'dashjdj': 'ffhhdvnndj',
                   'dhfhdfjnff': 'dhdhhgfhfg',
                   'vinay': 'vinaykumar',
                   'rytghdhhf': 'rujfjdhjjf',
                   'dkjdjfjjfjhd': 'kdjfjjhhf'}


def OtpGenerator():
    otp = random.randint(100000, 999999)
    return otp


def login():
    username = input('Enter your username : ')
    if username in userCredentials.keys():
        password = input('Enter your password : ')
        if userCredentials[username] == password:
            timer()
            print('Loading....Please Wait.')
            timer()
            print(OtpGenerator())
            otp = input('Enter the OTP : ')
            if len(otp) == 6:
                timer()
                print('Loading.... Please Wait.')
                timer()
                print('Login Successful....!!!!!!!')
            else:
                print('Wrong OTP... Login Failed!')
        else:
            print('Wrong Password...')


    else:
        print('Username is wrong!!!')
