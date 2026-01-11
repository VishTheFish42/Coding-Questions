'''
IS ANAGRAM
Given two strings, return whether or not the two are anagrams of one another.
'''

def is_anagram(s1, s2):
    s1_hash = Counter(s1)
    s2_hash = Counter(s2)
    return s1_hash == s2_hash
