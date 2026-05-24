#Store my_num as [1, 4, 7, 9, 12, 18]. Used filter function to select multiple of 3.
#Store my_num as [1, 4, 7]. Used map function to calculate cube of each number.
#Store my_num as [1, 5, 7, 9]. Used reduce function to calculate product of these.

my_num = [1, 4, 7, 9, 12, 18]
filtered_data = filter(lambda x: x%3 ==0,my_num)
print(filtered_data)

my_num = [1, 4, 7]
cube_num = map(lambda x: x**3,my_num)
print(list(cube_num))

from functools import reduce
my_num = [1, 5, 7, 9]
product = reduce(lambda x ,y: x*y,my_num)
print(product)



