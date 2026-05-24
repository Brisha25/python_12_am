# Ask user for string and check if it's palindrome in format: "madam" is [not] a palindrome
str_1 = input("enter for string: ")
if str_1[:-1]:
   print(f"{str_1} is a palindrome")
else:
    print(f"{str_1} is not palindrome")