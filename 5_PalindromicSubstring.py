# Prompt: Given a string s, return the longest palindromic substring in s.
# Optimised

import time
starttime = time.time()

def LongestPalindromicSubstring(s):
    longest = 0
    substring = ""
    s = s.lower()
    # makes the string lowercase in case there are letters that are upper case as this wont count as a palindrome otherwise

    for i in range(len(s)):
        # goes through every letter to be the start of the substring

        for j in range(i + longest, len(s) + 1):
            # goes until the length plus 1, because when taking a substring using [:x], it does not include the xth index
            # it goes through the rest of the letters after i, because it does not need to go through the letters before i again
            # it starts at i + longest, because it doesnt need to check all the substrings that have fewer characters than the current longest

            if IsPalindrome(s[i:j]):
                # if the substring from index i (including) to index j (excluding) is a palindrome

                if len(s[i:j]) > longest:
                    # if it is the longest one yet then replace the variables
                    longest = len(s[i:j])
                    substring = s[i:j]

    print(longest, substring)


def IsPalindrome(s):
    palindrome = True
    for i in range(1, len(s)):
        if s[i] != s[-(i+1)]:
            palindrome = False
            # if the letters at opposite indexes are not the same, then it is not a substring
            break
            # breaks to go to the next substring
    return palindrome
        
s = "iohdghlabcdefghijklmnopqrstuvwxykjbnlkjfdklffffffffkdfopeifklsppowihdfdsvbsubdvhdbvjkbkjnoifebpejgvmpweflkndgkajdfklsbdbgbkdkbgbjbglkbdvllvdbklgbjbgbkdkbgbdbslplkjadggsdkljvbjvjhoiphsofdjkglgdjfkldhfkiohdghlabcdefghijklmnopqrstuvwxykjbnlkjfdklffffffffkdfopeifklsppowihdfdsvbsubdvhdbvjkbkjnoifebpejgvmpweflkndgkajdfklsbdbgbkdkbgbjbglkbdvllvdbklgbjbgbkdkbgbdbslplkjadggsdkljvbjvjhoiphsofdjkglgdjfkldhfkiohdghlabcdefghijklmnopqrstuvwxykjbnlkjfdklffffffffkdfopeifklsppowihdfdsvbsubdvhdbvjkbkjnoifebpejgvmpweflkndgkajdfklsbdbgbkdkbgbjbglkbdvllvdbklgbjbgbkdkbgbdbslplkjadggsdkljvbjvjhoiphsofdjkglgdjfkldhfkiohdghlabcdefghijklmnopqrstuvwxykjbnlkjfdklffffffffkdfopeifklsppowihdfdsvbsubdvhdbvjkbkjnoifebpejgvmpweflkndgkajdfklsbdbgbkdkbgbjbglkbdvllvdbklgbjbgbkdkbgbdbslplkjadggsdkljvbjvjhoiphsofdjkglgdjfkldhfkiohdghlabcdefghijklmnopqrstuvwxykjbnlkjfdklffffffffkdfopeifklsppowihdfdsvbsubdvhdbvjkbkjnoifebpejgvmpweflkndgkajdfklsbdbgbkdkbgbjbglkbdvllvdbklgbjbgbkdkbgbdbslplkjadggsdkljvbjvjhoiphsofdjkglgdjfkldhfk"

LongestPalindromicSubstring(s)
print(time.time() - starttime)