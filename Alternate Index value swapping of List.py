n=int(input("Enter no.of elemnets you want to add in the list : "))
val=[] 
for i in range(n):
    v=input("Enter value = ")
    val.append(v)
print("Original List : ",val)
print("Swapping Even index values with odd index values.....")
#Swapping Even index values with odd index values 
for i in range(0,n-1,2):
    val[i],val[i+1]=val[i+1],val[i]
print("Swapped List :",val)