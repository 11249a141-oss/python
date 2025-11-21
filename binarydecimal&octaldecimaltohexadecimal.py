//Aim:
To develop a Python program that converts:
A binary number to its decimal equivalent.
An octal number to its hexadecimal equivalent,
using user-defined functions.
//Algorithm:
Start the program.
Define a function binary_to_decimal(binary) that:
Takes a binary number as input.
Converts it to decimal using int(binary, 2).
Returns the decimal value.
Define another function octal_to_hexadecimal(octal) that:
Takes an octal number as input.
Converts it to hexadecimal using hex(int(octal, 8)).
Returns the hexadecimal value.
Ask the user to enter a binary number.
Ask the user to enter an octal number.
Call the two functions with the given inputs.
Display the converted decimal and hexadecimal results.
End the program.
//program:
def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def octal_to_hexadecimal(octal):
    hexadecimal = hex(int(octal, 8))
    return hexadecimal.upper()


binary_num = input("Enter a binary number: ")
octal_num = input("Enter an octal number: ")

decimal_result = binary_to_decimal(binary_num)
hexadecimal_result = octal_to_hexadecimal(octal_num)

print("\n--- Conversion Results ---")
print(f"Binary to Decimal: {binary_num} → {decimal_result}")
print(f"Octal to Hexadecimal: {octal_num} → {hexadecimal_result}")
//result:
the bove program conversion of binarydecimal and octaldecimal to hexadecimal is executed successfully
