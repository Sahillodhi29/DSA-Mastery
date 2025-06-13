def is_palindrome(s):
    if len(s) <=1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False
    

s= "racepcar"

print(is_palindrome(s))

print(is_palindrome("madam"))      # True
print(is_palindrome("python"))     # False
print(is_palindrome("a"))          # True
print(is_palindrome("")) 