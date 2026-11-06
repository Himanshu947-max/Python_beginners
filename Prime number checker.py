n=int(input("Enter any number= "))
if n<2:
    print("It is not a Prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("It is not a Prime number")
            break
        else:
            continue
    else:
         print("It is a Prime number")    
