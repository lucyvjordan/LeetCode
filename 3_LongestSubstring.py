# Prompt: Given a string s, find the length of the longest substring without repeating characters.

import time
starttime = time.time()

def LongestSubstring(s):
    longest = 0
    current = 0
    letters = []
    for i in range(len(s)):
        if s[i] in letters:
            # if the current letter has already appeared in the substring
            letters = [s[i]]
            # reset the substring to start at the current letter, so the letters array must contain the current letter
            if current > longest:
                # if the current substring is longer than the current longest one found, set longest equal to current
                longest = current
            current = 1
            # the current substring now only has 1 letter: the current letter
        else:
            current += 1
            letters.append(s[i])
            # if not in letters, increment current and append the letter to the letters array
    print(longest)
        
s = "abcabcbb"
LongestSubstring(s)
print(time.time() - starttime)