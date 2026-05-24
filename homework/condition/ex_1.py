user_name = input("enter for name: ")
birth_year = int(input("enter for birth year"))

if birth_year >= 18:
  print(f"{user_name}, You are eligible for voting.")
else:
    print(f"{user_name}, you are not eligible for voting.")

