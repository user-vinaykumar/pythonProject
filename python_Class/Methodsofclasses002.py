# regular / instance methods, class methods and static methods.


import random
import time

class Moviebooking:

    ticket = 500
    movieLanguage = input('Enter the language of the movie: ')
    movieName = input('Enter the movie name : ')
    seatCount = 0

    kannada = ['KGF', 'Kantara', 'Kaatera', 'Blink', 'Shaakahaari', 'SSE']
    tamil = ['Leo', 'Jai Bheem', 'Jailer', 'Thunivu', 'Mark Antony']
    telugu = ['Aadipurush', 'OG', 'Salaar', 'Bheema', 'Kick']

    def __init__(self, numOfTickets):
        self.numOfTickets = numOfTickets

        Moviebooking.seatCount += 1

    @classmethod
    def kanLangMov(cls, itemkan):
        cls.kannada = itemkan

    @classmethod
    def tamilLangMov(cls, itemtam):
        cls.tamil = itemtam

    @classmethod
    def teluguLangMov(cls, itemtel):
        cls.telugu = itemtel

    @staticmethod
    def selectLanguage(item):
        if item.upper() == 'KANNADA':
            return Moviebooking.kannada
        elif item.upper() == 'TAMIL':
            return Moviebooking.tamil
        elif item.upper() == 'TELUGU':
            return Moviebooking.telugu
        else:
            print(f'The language you entered is not in the website')
            return False

    @staticmethod
    def movieIntheList(item1, item2):
        if item1 in item2:
            return True
        else:
            print(f'Movie you entered is not in the website')
            return False

    @staticmethod
    def creditcardpayment(item):
        if len(item) == 8:
            cccvv = input('Enter the cvv of the credit card: ')
            if len(cccvv) == 3:
                return 'card validated successfully'
            else:
                return 'wrong cvv number'
        else:
            return 'card number is wrong'



    @staticmethod
    def debitcardpayment(item):
        if len(item) == 8:
            dbvv = input('Enter the cvv number: ')
            if len(dbvv) == 3:
                return 'card validated successfully'
            else:
                return 'wrong cvv number'
        else:
            return 'wrong card number'



    @staticmethod
    def selectcard(item):
        if item.upper() == 'CREDIT':
            ccnumber = input('Enter the card number: ')
            time.sleep(3.0)
            return Moviebooking.creditcardpayment(ccnumber)
        elif item.upper() == 'DEBIT':
            dbnumber = input('Enter the card number: ')
            time.sleep(3.0)
            return Moviebooking.debitcardpayment(dbnumber)
        else:
            return f'Enter the card you want to pay'

    @staticmethod
    def otpvalidation(items):
        if len(items) == 6:
            return 'OTP validated successfully'
        else:
            return 'Entered OTP is wrong'

    @staticmethod
    def pay(items):
        price = Moviebooking.ticket * items
        card = input('credit/debit: ')
        time.sleep(3.0)
        if card.upper() == 'CREDIT' or 'DEBIT':
            Moviebooking.selectcard(card)
            time.sleep(3.0)
            otp = random.randint(100000, 1000000)
            print(f'here is your OTP : {otp}')
            time.sleep(3.0)
            enterotp = input('Enter the otp received : ')
            time.sleep(3.0)
            Moviebooking.otpvalidation(enterotp)
            print(f'{price} has been deducted from your account via online payment for {items} tickets')
        else:
            print(f'Select the appropriate card first')










    def bookMovie(self):
        movielang = self.movieLanguage
        movietitle = self.movieName
        if self.selectLanguage(movielang):
            if self.movieIntheList(movietitle, self.selectLanguage(movielang)):
                time.sleep(3.0)
                print(f'Wait the process is loading...')
                time.sleep(3.0)
            else:
                return f'Movie you entered is not in the {movielang} list'
        else:
            return f'Entered language is not in the website'
        self.pay(self.numOfTickets)

vinay = Moviebooking(3)
vinay.bookMovie()






