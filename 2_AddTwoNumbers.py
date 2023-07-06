""" Prompt: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. """

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

l1 = [9,9,9,9]
l2 = [9,9,9,9,9,9,9]
AddLists(l1, l2)
print(time.time() - starttime)

