file_name = "report_2026.pdf"
my_date = "2026-03-05"
split = my_date.split("-")
print(split)
print("year",my_date[0:4])
print("month",my_date[5:7])
print("day",my_date[8::])
my_str="PYTHON"
result = (".").join(my_str)
print(result)
laptop_names=["Dell","HP","Apple"]
result=("-").join(laptop_names)
print(result)
str_1 = "Hello , World!"
result = str_1.replace("World","Python")
print(result)
str_2 = "2026-03-01.csv"
result= str_2.replace("-","/")
print(result)
str_3 = "Pineapple"
index = str_3.find("apple")
print(index)
my_name = "brisha shrestha"
my_name = my_name.lower()
vowel_count = my_name.count("a")+my_name.count("e")+my_name.count("i")+my_name.count("o")+my_name.count("u")
print(vowel_count)
my_str="Hello,World!"
count = my_str.count("l")
print(count)