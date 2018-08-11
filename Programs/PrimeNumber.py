#This program checks wheather the entered number is prime or not

def checkPrime(number):
    '''This fucntion checks for prime number'''
    isPrime=False
    if number==2:
        print(number,'is a Prime Number')

    if number>1:
        for i in range(2,number):
            if number%i==0:
                print(number,'is not a prime number')
                isPrime=False
                break
            else:
                isPrime=True
        if isPrime:
            print(number,'is a Prime Number')

if __name__=='__main__':
    userInput=int(input('Enter a number to check:'))
    checkPrime(userInput)
