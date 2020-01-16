#This program checks wheather entered number is prime or not

def checkPrime(number):
    '''This funciton checks for prime number'''
    if number==1:
       print(number,'is not a prime number')
    elif number==2:
       print(number,'is prime number')
    else:
       for i in range(2,number):
           if number%i==0:
               print(number,'is not a prime number')
       print(number, 'is a prime number')
number=int(input())

checkPrime(number)