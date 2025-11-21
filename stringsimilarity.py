//Aim:
To write a Python program that finds the similarity between two given strings using a suitable method such as SequenceMatcher from the difflib module.
 
//Algorithm:
1.Start the program.
2.Import the SequenceMatcher class from the difflib module.
3.Read two input strings from the user.
4.Use SequenceMatcher(None, string1, string2) to compare the two strings.
5.Get the similarity ratio using .ratio() method.
6.Display the similarity percentage by multiplying the ratio by 100.
7.Stop the program.
//program:
from difflib import SequenceMatcher

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

similarity = SequenceMatcher(None, str1, str2).ratio()

print(f"Similarity between the two strings: {similarity * 100:.2f}%")
//result:
   the above program similarity between two strings using a suitable method is successfully executed
