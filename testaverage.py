//Aim:To write a Python program that accepts marks of three tests from the user and calculates the best two test average among them.
//Algorithm:
1.Start the program.
2.Accept three test marks from the user.
3.Store them in three variables — test1, test2, and test3.
4.Find the total of all three marks.
5.Subtract the smallest mark (i.e., the lowest score) from the total.
6.Divide the remaining total by 2 to get the average of the best two tests.
7.Display the average.
8.Stop the program.
//program:
test1 = float(input("Enter marks of Test 1: "))
test2 = float(input("Enter marks of Test 2: "))
test3 = float(input("Enter marks of Test 3: "))
total = test1 + test2 + test3
lowest = min(test1, test2, test3)
best_two_total = total - lowest
average = best_two_total / 2

print("Average of best two tests =", average)
//result:program to find the best of two averages out of three marks is successfullly completed and executed.

