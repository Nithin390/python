a = str(input("enter first string : "))
b = str(input("enter second string : "))
strlength = len(a)
count = 0
for i in range(strlength):
    if(a[i] == b[i]):
        count +=1
print("number of matches : ",count)
 
