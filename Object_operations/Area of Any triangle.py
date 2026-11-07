s1=float(input("Enter First side of triangle="))
s2=float(input("Enter Second side of triangle="))
s3=float(input("Enter Third side of triangle="))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    s=(s1+s2+s3)/2
    Area=(s*(s-s1)*(s-s2)*(s-s3))**(0.5)
    print("Area of Triangle=",Area)
else:
    print("invalid triangle")
    