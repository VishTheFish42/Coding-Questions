'''
CHAPTER 1
Arrays and Strings

PROBLEM 1.1
Is Unique

DESCRIPTION
Implement an algorithm to determine if a string has all unique characters.
'''
def is_unique(s):
    s_letter_hash = {}

    for letter in s:
        if letter in s_letter_hash:
            return False
        else:
            s_letter_hash[letter] = 1
    
    return True

'''
EXTENSION
What if you cannot use additional data structures?
'''
