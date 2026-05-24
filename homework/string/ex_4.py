str_1 = "Hello"
str_2 = "12345"
str_3 = "###abc123###"
str_4 = " "
is_alpha = str_1.isalpha()
print(is_alpha)
is_num = str_1.isnumeric()
print(is_num)
is_alnum = str_2.isalnum()
print(is_alnum)
is_space = str_4.isspace()
print(is_space)
starts_with = str_3.startswith("abc")
print(starts_with)
ends_with = str_3.endswith("3")
print(ends_with)
starts_with = str_1.startswith("He") and str_1.endswith("lo")
print(starts_with)
clean_str_1 = str_3.lstrip("#")
print(clean_str_1)
clean_str_2 = str_3.strip("#")
print(clean_str_2)


