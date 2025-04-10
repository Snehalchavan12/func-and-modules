# func-and-modules
#Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
  
    def fact(n):
    
    return 1 if (n==1 or n==0) else n * fact(n - 1) 
    num =int (input ('Enter the number:' ))
    print ('factorial of number is')
    print (fact(num))

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

    import math
   
    number = 20
   
    square_root = math.sqrt(number)
   
    print(f"The square root of {number} is {square_root}")

    log_value = math.log(number, 2)  # Logarithm base 2
  
    print(f"The logarithm of {number} is {log_value}")
  
    sin_value = math.sin(number)
    
    print("Sin:", sin_value)
