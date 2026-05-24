stds_info = [["Brisha","16"],["Susma","17"]]
print(stds_info[1][-1])
marks_list =[ 70,56,89,93,94]
subject_list =["Math","science","english","nepali","account"]
total = sum(marks_list)
print(f"Total marks: {total}")
total = sum(marks_list)/5
print(f"Average: {total}")
min_value = min(marks_list)
print(f"Lowest marks: {min_value}")
max_value = max(marks_list)
print(f"highest value: {max_value}")
third_position = marks_list[2]
print(f"Marks obtained in English is {third_position}")
fourth_position = marks_list[3]
print(f"Marks obtained in nepali is {fourth_position}")
marks = marks_list[3:]
print(f"Mrks obtained in last two subjects are {marks}")
marks = marks_list[0:3]
print(f"Marks obtained in first three subjects are {marks}")
highest_score_subject = subject_list[4]
print(f"Highest score subject is {highest_score_subject}")
Lowest_score_subject = subject_list[1]
print(f"Lowest score subject is {Lowest_score_subject}")

