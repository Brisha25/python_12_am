user_name = input("enter for name: ")
print(f"Hello, <{user_name}>!")
birth_year = int(input("enter for birth year: "))
age = 2083 - birth_year
print(f"my age is {age}")
mass = int(input("enter for mass: "))
length = int(input("enter for length: "))
density = mass/length*3
print(f"{density}")
length_in_ft = float(input("enter for length: "))
length_in_m = length_in_ft*0.3048
print(f"{length_in_m}")
file_name = ("enter for file name")
splitted_data = file_name.split(".")
print(splitted_data[-1])
