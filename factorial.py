def fact(n):
    
    return 1 if (n==1 or n==0) else n * fact(n - 1) 
num =int (input ('Enter the number:' ))
print ('factorial of number is')
print (fact(num))