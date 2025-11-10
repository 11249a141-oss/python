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