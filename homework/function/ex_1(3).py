#Write a function is_palindrome(string) to check if a given string is palindrome or not. 
#Return True if it is palindrome else return False.
def is_palindrome(string):
    reverse = string[::-1]
    if string.lower() == reverse.lower():
        return True
    else:
        return False

chk = is_palindrome('Rar')
print(chk)