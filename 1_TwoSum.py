# Prompt: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [3, 3, 4]
target = 6

def findSum(nums, target):
    
    newnums = list(filter(lambda x: x < target, nums))
    # filters numbers to those less than the target to reduce runtime

    for i in range(len(newnums)):
        # goes through every number less than the target
        for j in range(i, len(newnums) - 1):
            # goes through every other number less than the target after the first number (so that sums are not attempted multiple times)
            if newnums[i] + newnums[j + 1] == target:
                if newnums[i] == newnums[j + 1]:
                    # if the two numbers are the same
                    indexes = [index for index, value in enumerate(nums) if value == newnums[i]]
                    # find the two indexes where the number occurs
                    print(indexes[0], indexes[1])
                    # only prints the first two in case the number occurs more than twice
                else:
                    print(nums.index(newnums[i]), nums.index(newnums[j + 1]))
                    # if different numbers, print the indexes of the numbers where they occur in the original array
                return
            
findSum(nums, target)

