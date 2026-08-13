'''
PROBLEM 1.5
One Away

DESCRIPTION
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale,  ple  -> true
pales, pale -> true
pale,  bale -> true
pale,  bake -> false
'''

from collections import Counter

def one_away(s1, s2):
  if (abs(len(s1) - len(s2)) > 1):
    return False

  if (len(s1) == len(s2)):
    diff_char_count = 0

    for i in range(0, len(s1)):
      if (s1[i] != s2[i]):
        diff_char_count += 1
        if (diff_char_count > 1):
          return False

    return True

  else:
    if (len(s2) > len(s1)):
      s1, s2 = s2, s1

    for i in range(0, len(s1)):
      if (s1[:i] + s1[i + 1:] == s2):
        return True

    return False

'''
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the length of the longer string
'''
