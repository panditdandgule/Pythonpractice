# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
n=int(input())

n1=0
n2=1
count=0


if n<=0:
    print("Please enter a positive number")
elif n==1:
    print('Fibonacci sequance upto:',n)
    print(n1)
else:
    print('Fibonacci sequance upto:',n)
    while count<n:
        print(n1,end=', ')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1




