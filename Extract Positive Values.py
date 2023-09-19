list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Input: list1 =", list1)
print("Output:", end=" ")
positive_numbers1 = [num for num in list1 if num > 0]
if positive_numbers1:
    print("output: ", positive_numbers1)
else:
    print("No positive numbers found in the list.")

print("Input: list2 =", list2)
positive_numbers2 = [num for num in list2 if num > 0]
if positive_numbers2:
    print("output: ", positive_numbers2)
else:
    print("No positive numbers found in the list.")