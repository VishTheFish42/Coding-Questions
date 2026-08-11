'''
PROBLEM 1.4
Palindrome Permutation

DESCRIPTION
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: 		Tact Coa
Output: 	True (permutations: “taco cat”, “atco cta”, etc.)
'''

from collections import Counter

def palindrome_permutation(s):
  no_spaces_s = s.replace(' ', '')
  s_hash = Counter(no_spaces_s.lower())

  odd_found = False
  
  for letter in s_hash:
    if (s_hash[letter] % 2 == 1):
      if (odd_found):
        return False
      odd_found = True

  return True

'''
ASSUMPTIONS
[1] The input string contains only uppercase and lowercase characters.
[2] Palindromes are determined on a case-insensitive basis.
[3] Spaces are not counted in the determination of a palindrome.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the length of the string
'''

from collections import Counter

def palindrome_permutation(s):
  s_hash = Counter(s)

  odd_found = False
  
  for letter in s_hash:
    if (s_hash[letter] % 2 == 1):
      if (odd_found):
        return False
      odd_found = True

  return True

'''
ASSUMPTIONS
[1] The input string contains any characters.
[2] Palindromes are determined on a case-sensitive basis.
[3] Spaces are counted in the determination of a palindrome.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the length of the string
'''
