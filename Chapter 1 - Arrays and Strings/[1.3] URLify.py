'''
PROBLEM 1.3
URLify

DESCRIPTION
Write a method to replace all spaces in a string with ‘%20’. 
You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the “true” length of the string. 
(Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

EXAMPLE
Input: 		“Mr John Smith    ”, 13
Output: 	“Mr%20John%20Smith”
'''

def URLify(s, true_length):
  actual_s = s[:true_length]
  url_list = ['%20' if (character == ' ') else character for character in actual_s]
  return ''.join(url_list)

'''
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the "true" length of the string
'''

def URLify2(s, true_length):
  num_spaces = 0

  for i in range(0, true_length):
    if (s[i] == ' '):
      num_spaces += 1

  final_s_length = true_length + (num_spaces * 2)
  final_s_index = final_s_length - 1
  true_s_index = true_length - 1

  while (true_s_index >= 0):
    if (s[true_s_index] == ' '):
      s[final_s_index] = '0'
      s[final_s_index - 1] = '2'
      s[final_s_index - 2] = '%'
      final_s_index -= 3
    else:
      s[final_s_index] = s[true_s_index]
      final_s_index -= 1

    true_s_index -= 1

  return s[:final_s_length]

'''
ASSUMPTIONS
[1] There are not EXACTLY enough characters at the end, but a SUFFICIENT number.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(1)
where n is the “true” length of the string
'''
