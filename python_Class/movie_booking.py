# # create a class for movie booking and its processes.
#
# import time
# import random
#
# class Moviebooking:
#
#
#     # movieLanguage = input('Enter the language you want to book a movie for:')
#     # moviename = input('Enter the movie you want to book:')
#     # numberOfTickets = int(input('Enter the number of tickets to be booked:'))
#
#     def __init__(self, movieLanguage, moviename, numberOfTickets):
#         self.movieLanguage = movieLanguage
#         self.moviename = moviename
#         self.numberOfTickets = numberOfTickets
#
#
#
#     kannada = {'KGF', 'Kantara', 'Rajakumara', 'Yuva', 'Kaatera', 'KGF2', 'SSE'}
#     telugu = {'Bahubali', 'Aadipurush', 'Gabbarsingh', 'Magadheera', 'Aarya', 'Aarya2'}
#     tamil = {'Singham1', 'Paiya', 'Leo', 'Thunivu', 'Jai Bheem', 'Jailer', 'Vikram'}
#     malayalam = {'Premam', 'Jojo', 'Lucifer', 'Premalu', 'Bangalore Days', 'Bramayugam'}
#
#     def otp(self):
#         return random.randint(100000, 1000000)
#
#     def cardvalidation(self, carddetail1, carddetail2):
#         if type(carddetail1) == str:
#             if len(carddetail1)>3:
#                 time.sleep(4.0)
#                 print(f'wait!!! Processing the CVV.....')
#                 time.sleep(3.0)
#                 if len(carddetail2) == 3:
#                     print(f'Card validated successfully...')
#                     return True
#                 else:
#                     print(f'Entered wrong CVV..')
#                     return False
#             else:
#                 print(f'Wrong card number...')
#                 return False
#         else:
#             print(f'This card does not exist...')
#             return False
#
#
#
#
#     def debitcardpay(self, ticketsum1):
#         debitticketprice = 500
#         debitcardno = (input('Enter the debit card number :'))
#         debitcvv = (input('Enter the cvv :'))
#         if self.cardvalidation(debitcardno, debitcvv) == True:
#             debitticketprice*=ticketsum1
#             time.sleep(3.0)
#             paypricedb = input(f'ready to pay the ticket {debitticketprice} enter y/n :')
#             if paypricedb.upper() == 'Y':
#                 time.sleep(3.0)
#                 print(f'This is your OTP : {self.otp()}')
#                 time.sleep(3.0)
#                 enterOTP = input('Enter the OTP received :')
#                 if self.otpvalidation(enterOTP) == True:
#                     return 'PAYMENT DONE SUCCESSFULLY'
#                 else:
#                     return 'WRONG OTP'
#             else:
#                 return 'PAYMENT CANCELLED'
#
#
#
#
#
#     def creditcardpay(self, ticketsum2):
#         creditticketprice = 500
#         creditcardno = (input('Enter your credit card number :'))
#         creditcvv = (input('Enter the cvv :'))
#         if self.cardvalidation(creditcardno, creditcvv) == True:
#             creditticketprice *= ticketsum2
#             time.sleep(3.0)
#             paypricecc = input(f'ready to pay the ticket {creditticketprice} enter y/n :')
#             if paypricecc.upper() == 'Y':
#                 time.sleep(3.0)
#                 print(f'this is your OTP :{self.otp()}')
#                 time.sleep(3.0)
#                 enterOTP = input('Enter the OTP recieved:')
#                 if self.otpvalidation(enterOTP) == True:
#                     return 'PAYMENT DONE SUCCESSFULLY'
#                 else:
#                     return 'WRONG OTP'
#             else:
#                 return 'PAYMENT CANCELLED'
#
#
#
#
#
#     def upipay(self, ticketsum3):
#         pass
#
#
#
#
#     def pay(self, tickets):
#         if tickets > 0:
#             time.sleep(4.0)
#             ticketpay = input('credit card / debit card / UPI :')
#             time.sleep(3.0)
#             if ticketpay == 'credit card':
#                 return self.creditcardpay(tickets)
#             elif ticketpay == 'debit card':
#                 return self.debitcardpay(tickets)
#             elif ticketpay == 'UPI':
#                 return self.upipay(tickets)
#             else:
#                 return 'Enter the payment method.'
#         else:
#             return 'Select the tickets.'
#
#
#
#     def selectMovieList(self, item):
#         if item.upper() == 'KANNADA':
#             return self.kannada
#         elif item.upper() == 'TELUGU':
#             return self.telugu
#         elif item.upper() == 'TAMIL':
#             return self.tamil
#         elif item.upper() == 'MALAYALAM':
#             return self.malayalam
#         else:
#             return 'Enter only South Indian Languages to book the ticket.'
#
#
#
#     def selectMovies(self):
#         self.movieLanguage = input('Enter the language you want to book a movie for :')
#         self.moviename = input('Enter the movie you want to book :')
#         if self.moviename in self.selectMovieList(self.movieLanguage):
#             time.sleep(4.0)
#             print(f'wait...the process is loading!!!!')
#             time.sleep(3.0)
#             self.numberOfTickets = int(input('Enter the number of tickets to be booked :'))
#             self.pay(self.numberOfTickets)
#
#         else:
#             time.sleep(4.0)
#             return 'Movie you are looking is not in the website..'
#
#     def otpvalidation(self, onetimepassword):
#         onetp = onetimepassword
#         if onetimepassword == onetp:
#             return True
#         else:
#             return False
#
#
# bookMyShow = Moviebooking('','',0)
# bookMyShow.selectMovies()