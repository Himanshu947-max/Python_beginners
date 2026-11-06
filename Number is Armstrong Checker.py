n=int(input("Enter any number="))
num=n
arm=0
while(num>=1):
    r=num%10
    num=num//10
    arm=(r**3)+arm
print("After Checking=",arm)
if arm==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")