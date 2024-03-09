# create a class for movie booking and its processes.

import time
import random

class Moviebooking:

    def __init__(self):
        pass

    kannada = {'KGF', 'Kantara', 'Rajakumara', 'Yuva', 'Kaatera', 'KGF2', 'SSE'}
    telugu = {'Bahubali', 'Aadipurush', 'Gabbarsingh', 'Magadheera', 'Aarya', 'Aarya2'}
    tamil = {'Singham1', 'Paiya', 'Leo', 'Thunivu', 'Jai Bheem', 'Jailer', 'Vikram'}
    malayalam = {'Premam', 'Jojo', 'Lucifer', 'Premalu', 'Bangalore Days', 'Bramayugam'}


    def cardvalidation(self, carddetail1, carddetail2):
        if type(carddetail1) == int:
            if len(carddetail1)>3:
                time.sleep(4.0)
                print(f'wait!!! fetching data from the database.....')
                time.sleep(3.0)
                return ''




    def debitcardpay(self):
        debitcardno = int(input('Enter the debit card number : '))
        debitcvv = int(input('Enter the cvv : '))


    def creditcardpay(self):
        creditcardno = int(input('Enter your credit card number : '))
        creditcvv = int(input('Enter the cvv : '))

    def upipay(self):
        upinumber = int(input('Enter the upi id number : '))



    def pay(self, tickets):
        if tickets > 0:
            time.sleep(4.0)
            ticketpay = input('credit card / debit card / UPI : ')
            time.sleep(3.0)
            if ticketpay == 'credit card':
                self.creditcardpay()
            elif ticketpay == 'debit card':
                self.debitcardpay()
            elif ticketpay == 'UPI':
                self.upipay()



    def selectMovieList(self, item):
        if item.upper() == 'KANNADA':
            return self.kannada
        elif item.upper() == 'TELUGU':
            return self.telugu
        elif item.upper() == 'TAMIL':
            return self.tamil
        elif item.upper() == 'MALAYALAM':
            return self.malayalam
        else:
            return 'Enter only South Indian Languages to book the ticket.'



    def selectMovies(self):
        movieLanguage = input('Enter the language you want to book a movie for : ')
        movieName = input('Enter the movie you want to book : ')
        if movieName in self.selectMovieList(movieLanguage):
            time.sleep(4.0)
            print(f'wait...the process is loading!!!!')
            time.sleep(3.0)
            numberOfTickets = int(input('Enter the number of tickets to be booked : '))
            self.pay(numberOfTickets)

        else:
            time.sleep(4.0)
            return 'Movie you are looking is not in the website..'

