x = int(input("Enter a number: "))  
result = "--" 
for num in range(1, 10):  
    if num % x == 0 or str(x) in str(num):  
        continue  
    result.append(num)  
if num % 4 == 0 and num % 10 != 0:
    print('Число кратно 4 и не кратно 10.')
     