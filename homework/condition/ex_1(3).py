user_name = input("enter for name: ")
user_age = int(input("enter for age: "))
user_salary = int(input("enter for salary: "))
if user_age > 21 and user_age < 60 and user_salary >= 30000:
   print(f"{user_name}, You are eligible for loan")
else:
    print(f"{user_name}, You are not eligilbe for loan")