//Aim:
To write a Python program that accepts a sentence and finds the number of:
Words
Digits
Uppercase letters
Lowercase letters
//Algorithm:
Start the program.
Input a sentence from the user.
Initialize counters for words, digits, uppercase letters, and lowercase letters to zero.
Split the sentence into words using the split() function to count the number of words.
Loop through each character in the sentence:
If the character is a digit, increment the digit counter.
If the character is an uppercase letter, increment the uppercase counter.
If the character is a lowercase letter, increment the lowercase counter.
Display all the counts.
End the program.
//program
def sentence_statistics(sentence):
    words = len(sentence.split())
    digits = 0
    uppercase = 0
    lowercase = 0

    for ch in sentence:
        if ch.isdigit():
            digits += 1
        elif ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1

    return words, digits, uppercase, lowercase

sentence = input("Enter a sentence: ")

words, digits, uppercase, lowercase = sentence_statistics(sentence)

print("\n--- Sentence Statistics ---")
print(f"Number of Words: {words}")
print(f"Number of Digits: {digits}")
print(f"Number of Uppercase Letters: {uppercase}")
print(f"Number of Lowercase Letters: {lowercase}")
//result: the above program sentencestatics is executed successfully
