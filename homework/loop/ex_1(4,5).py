#Assign list with numbers. Find the second largest number in it using for loop.
w list evaluated_data using for loop such that odd number is doubled and even number is tripled. If you encounter 4, skip evaluation for this and it you see 8, stop the loop.
numbers = [25 , 20 , 5 , 13 , 26]
highest = max(numbers)#Assign set as {1, 4, 5, 7, 8, 12}. Generate ne
second_highest = 0
for number in numbers:
    if number > second_highest and number < highest:
        second_highest = number

print(second_highest)