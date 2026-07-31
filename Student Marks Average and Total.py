Name=input("Enter Student Name:")
cl=input("Grade in which you are studying: ")
s1=float(input("Enter marks obtained in First Subject="))
s2=float(input("Enter marks obtained in Second Subject="))
s3=float(input("Enter marks obtained in Third Subject="))
s4=float(input("Enter marks obtained in Fourth Subject="))
s5=float(input("Enter marks obtained in Fifth Subject="))
if -1<s1<=100 and -1<s2<=100 and -1<s3<=100 and -1<s4<=100 and -1<s5<=100 :
    total=s1+s2+s3+s4+s5
    avg=total/5
    print("+---------------------------------------+")
    print("|\t\tREPORT CARD\t\t|")
    print(f"| Name: {Name:<32}|")
    print(f"| Grade: {cl:<31}|")
    print("|                                       |")
    print("|  Total Marks Obtained = ",total,"/500","     |",sep='')
    print("|  Average percentage = ",avg,"%","           |",sep='')
    print("|                                       |")
    print("+---------------------------------------+")
else:
    print("Enter marks out of 100")   
    #Updated With Borders
    #Added Class Input  
