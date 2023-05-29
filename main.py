"""Main functions"""


import re

def is_palindrome(string: str) -> bool:
    k_string = re.sub(r'[^a-zA-Z]', '', string.lower())
    return k_string == k_string[::-1]