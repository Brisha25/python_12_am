#Write a function get_rectangle_area_perimeter(length, width) 
#to calculate and return area and perimeter of a rectangle based on length and width.
def get_rectangle_area_perimeter(l,b):
    area = l*b
    perimeter = 2*(l+b)
    return area,perimeter

area,peri = get_rectangle_area_perimeter(15,5)
print(f"Area of rectangle with length of 15 and width of 5 is {area}")
print(f"perimeter of rectangle with length of 15 and width of 5 is {peri}")