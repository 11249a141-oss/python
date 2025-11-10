test1 = float(input("Enter marks of Test 1: "))
test2 = float(input("Enter marks of Test 2: "))
test3 = float(input("Enter marks of Test 3: "))
total = test1 + test2 + test3
lowest = min(test1, test2, test3)
best_two_total = total - lowest
average = best_two_total / 2
print("Average of best two tests =", average)