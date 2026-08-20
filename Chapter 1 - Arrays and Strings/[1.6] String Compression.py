'''
PROBLEM 1.6
String Compression

DESCRIPTION
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2b1c5a3. 
If the “compressed” string would not become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
'''

from collections import deque

def string_compression(s):
  if (len(s) <= 1):
    return s

  char_stack = deque([s[-1]])
  count_stack = deque([1])

  for i in range(len(s) - 2, -1, -1):
    if (s[i] == char_stack[-1]):
      count_stack[-1] += 1
    else:
      if (len(char_stack) == (len(s) // 2)):
        return s
      else:
        char_stack.append(s[i])
        count_stack.append(1)

  final_list = []
  cur_count = 0

  for i in range(len(char_stack)):
    final_list.append(char_stack.pop() + str(count_stack.pop()))
    if (cur_count + (len(final_list[-1])) >= len(s)):
      return s
    else:
      cur_count += len(final_list[-1])

  return ''.join(final_list)

'''
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the length of the string
'''
