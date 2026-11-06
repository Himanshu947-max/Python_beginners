s=input("Enter any string:")
c1=0
c2=0
sp=0
for i in s:
    if i.isalpha():
        c1=c1+1
    if i.isdigit():
        c2=c2+1
    else:
        sp=sp+1
print("No.of Alphabets=",c1)
print("No.of Digits=",c2)        
print("No.of Special symbols=",sp)
           