book_details = ["harry_potter","lord_of_rings","harry_potter"]
first_occurence = book_details[0]
print(first_occurence)
book = book_details.remove("harry_potter")
print(book)
book_name = ("enter for book name: ")
to_check = "book_name" in book_details
print(to_check)