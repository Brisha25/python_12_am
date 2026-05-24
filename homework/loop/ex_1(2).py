#Assign num_tuple as (1, 4, 7, 12, 20). Using loop, find even numbers and their sum

num_tuple = (1, 4, 7, 12, 20)
def is_even(num):
    remainder = num%2
    if remainder==0:
        return True
    else:
        return False
filtered_data = filter(is_even, num_tuple)
print(sum(filtered_data))
filtered_data = filter(is_even, num_tuple)
print(list(filtered_data))
