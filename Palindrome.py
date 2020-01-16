#This program checks for palindrome

def palindrome(string):
    '''This function checks the string for palindrome'''
    revString=string[::-1]
    if string==revString:
        print('String is palindrome')
    else:
        print('String is not palindrome')

if __name__=='__main__':
    userInput=str(input('Enter a string to check for Palindrome: '))
    palindrome(userInput)