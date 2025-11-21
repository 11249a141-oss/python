//Aim:To develop a Python program that converts:
1.A binary number to its decimal equivalent.
2.An octal number to its hexadecimal equivalent,using user-defined functions.
//Algorithm:
1.Start the program.
2.Define a function binary_to_decimal(binary) that:
3.Takes a binary number as input.
4.Converts it to decimal using int(binary, 2).
5.Returns the decimal value.
6.Define another function octal_to_hexadecimal(octal) that:
7.Takes an octal number as input.
8.Converts it to hexadecimal using hex(int(octal, 8)).
9.Returns the hexadecimal value.
10.Ask the user to enter a binary number.
11.Ask the user to enter an octal number.
12.Call the two functions with the given inputs.
13.Display the converted decimal and hexadecimal results.
14.End the program.
//Program:
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
//Result: a Python program that converts,A binary number to its decimal equivalent,An octal number to its hexadecimal equivalent,using user-defined functions executed succesfully
