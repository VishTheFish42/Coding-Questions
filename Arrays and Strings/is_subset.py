'''
IS SUBSET
Given two strings, determine whether the second string can be created using ONLY letters in the first string.
'''

def is_subset(s1, s2):
    if (len(s1) != len(s2)):
        return False
    
    s1_hash = {}

    for letter in s1:
        if letter in s1_hash:
            s1_hash[letter] += 1
        else:
            s1_hash[letter] = 1

    for letter in s2:
        if (letter not in s1_hash) or (s1_hash[letter] == 0):
            return False
        else:
            s1_hash[letter] -= 1

    return True
