//Aim:
To write a Python program that checks whether a given number is a palindrome or not and also counts the occurrence of each digit in the number.
//Algorithm:
1.Start the program.
2.Accept a number from the user.
3.Convert the number to a string for easy comparison and counting.
4.Reverse the string and check if it is the same as the original — if yes, it’s a palindrome; otherwise, it’s not.
5.Initialize an empty dictionary to store digit occurrences.
6.Traverse through each digit in the number:
7.If the digit is already in the dictionary, increase its count by 1.
8.Otherwise, add it to the dictionary with count 1.
9.Display whether the number is a palindrome or not.
10.Display each digit and its number of occurrences.
11.Stop the program.
//program:
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

    print(f"Digit {digit} occurs { freq } time(s).")
