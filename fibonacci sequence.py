//Aim:
To write a Python program that generates the Fibonacci sequence up to N terms, where N > 0. The program should display an error message if the entered value of N is not greater than zero.
//Algorithm:
Start the program.
Accept a value N from the user.
Check if N > 0:
If not, display an error message and stop the program.
Define a function fibonacci(N) to generate the Fibonacci sequence.
Inside the function:
Initialize the first two numbers as 0 and 1.
Use a loop to generate the next terms using the formula:
Fn = Fn-1 + Fn-2.
Print the sequence up to N terms.
Call the function with the user-provided value.
Stop the program.
//Program:
 
def fibonacci(N):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
 
 
N = int(input("Enter the number of terms (N > 0): "))
if N <= 0:
    print("Error: Please enter a value greater than 0.")
else:
   fibonacci(N)
//result: the above program fibonacci sequence upto N terms executes successfully
