//Aim:
To write a Python program that checks whether a given number is a palindrome or not and also counts the occurrence of each digit in the number.
//Algorithm:
Start the program.
Accept a number from the user.
Convert the number to a string for easy comparison and counting.
Reverse the string and check if it is the same as the original — if yes, it’s a palindrome; otherwise, it’s not.
Initialize an empty dictionary to store digit occurrences.
Traverse through each digit in the number:
If the digit is already in the dictionary, increase its count by 1.
Otherwise, add it to the dictionary with count 1.
Display whether the number is a palindrome or not.
Display each digit and its number of occurrences.
Stop the program.
//Program:
 
num = input("Enter a number: ")
 
 
if num == num[::-1]:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")
 
 
count = {}
for digit in num:
    if digit in count:
        count[digit] += 1
    else:
        count[digit] = 1
 
 
print("Digit occurrences:")
for digit, freq in count.items():
    print (f "Digit {digit} occurs { freq } time(s).")
//result:the palindrome program is excuted successfully
