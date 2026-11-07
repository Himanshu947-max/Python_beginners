s=input("Enter any string:")
a=0
for i in s:
    if i in('a','e','i','o','u','A','E','I','O','U'):
     a= a+1
print(s.count(a))