Name=input("Enter Student Name:")
s1=float(input("Enter marks obtained in First Subject="))
s2=float(input("Enter marks obtained in Second Subject="))
s3=float(input("Enter marks obtained in Third Subject="))
s4=float(input("Enter marks obtained in Fourth Subject="))
s5=float(input("Enter marks obtained in Fifth Subject="))
if -1<s1<=100 and -1<s2<=100 and -1<s3<=100 and -1<s4<=100 and -1<s5<=100 :
    total=s1+s2+s3+s4+s5
    avg=total/5
    print("Name:",Name)
    print("Total Marks Obtained (out of  500)=",total)
    print("Average percentage of All subject=",avg)
else:
    print("Enter marks out of 100")    
   
       