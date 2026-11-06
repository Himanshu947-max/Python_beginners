n=int(input("Enter any number="))
n_=n 
rev=0
while(n_>=1):
    r=n_%10
    n_=n_//10
    rev=rev*10+r
print("After reversing=",rev)    
if n==rev:
    print(rev,"is a Palindrome")
else:
    print(rev,"is not a Palindrome")    