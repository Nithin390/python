list1 = [2,5,10,13,8,7,6,9]
even_count,odd_count = 0,0
num = 0
while(num<len(list1)):
      if list1[num]%2 == 0:
                   even_count += 1
      else:
                   odd_count += 1
      num += 1
print("EVEN NUMBERS OF THE LIST ARE:",even_count)
print("ODD NUMBERS OF THE LIST ARE:",odd_count)
