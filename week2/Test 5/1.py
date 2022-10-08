def delchar(str,chr):
    val=""
    for i in str:
        if chr!=i:
            val+=i
    return val
value=input("Enter The String: ")
c=input("enter a character to be deleted: ")
new_str=delchar(value,c)
print("string after character removed: ",new_str)
        
