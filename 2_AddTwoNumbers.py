""" Prompt: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. """
# Optimised

import time
starttime = time.time()

def AddLists(l1, l2):
    num1 = ""
    num2 = ""
    for i in range(1, len(l1) + 1):
        # starts at 1, goes until the length of the linked list plus 1
        num1 += str(l1[-i])
        # the index counts from the end as the list is in reverse order, and adds the number to a string
    for j in range(1, len(l2) + 1):
        num2 += str(l2[-j])
    result = str(int(num1) + int(num2))

    l3 = []
    for k in range(1, len(result) + 1):
        # starts at 1, goes until the numbers of characters plus 1 in the result
        l3.append(int(result[-k]))
        # appends the character at the index (counting from the end again) as an int to the array
    print(l3)


l1 = [5, 2, 5, 0, 8, 5, 1, 5, 6, 1, 3, 3, 4, 1, 2, 9, 4, 5, 9, 6, 7, 4, 7, 4, 0, 1, 8, 1, 2, 5, 2, 8, 4, 0, 8, 5, 0, 4, 0, 6, 0, 2, 2, 8, 3, 0, 7, 1, 2, 7, 9, 8, 5, 4, 3, 2, 3, 6, 0, 3, 5, 1, 1, 7, 0, 6, 4, 0, 4, 6, 3, 6, 9, 7, 2, 7, 3, 5, 6, 9, 5, 2, 7, 9, 0, 0, 1, 7, 1, 5, 6, 8, 1, 9, 7, 5, 0, 6, 7, 2]
l2 = [0, 3, 1, 2, 8, 7, 2, 7, 5, 6, 3, 0, 9, 7, 5, 1, 2, 9, 1, 3, 6, 6, 5, 1, 7, 0, 4, 8, 0, 7, 4, 7, 2, 1, 2, 6, 5, 1, 7, 5, 7, 3, 6, 9, 2, 5, 5, 0, 7, 4, 9, 7, 7, 2, 9, 4, 7, 2, 7, 8, 4, 5, 3, 5, 2, 8, 3, 3, 0, 8, 1, 3, 2, 6, 9, 2, 9, 0, 4, 0, 3, 7, 9, 3, 9, 3, 4, 3, 3, 9, 5, 8, 7, 6, 5, 7, 9, 8, 4, 7]
AddLists(l1, l2)
print(time.time() - starttime)

