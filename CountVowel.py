def countVowel(sentance):
    '''This function counts the vowel'''
    count=0
    sentance=sentance.lower()
    for c in sentance:
        if c in ['a','e','i','o','u']:
            count+=1
    return count

if __name__=='__main__':
    userInput=str(input('Enter the string'))
    count=countVowel(userInput)
    print('Vowel Count',count)