# Prompt: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

import time
starttime = time.time()

def MedianOfArrays(nums1, nums2):
    nums3 = sorted(nums1 + nums2)
    # merge the two arrays and sort them
    
    if (len(nums3) / 2) % 2 == 0:
        # if the merged array has an even number of elements
        secondindex = len(nums3) / 2
        # the length / 2 will be the second index because indexes are counted from 0
        firstindex = secondindex - 1
        median = (nums3[int(firstindex)] + nums3[int(secondindex)]) / 2
        # the indexes are converted from floats to ints before being used as references
    else:
        index = len(nums3) // 2
        # the index when the array has an odd number of elements is found using the floor division of the length
        median = nums3[index]
    
    print(median)

nums1 = [1, 3]
nums2 = [2, 4]
MedianOfArrays(nums1, nums2)
print(time.time() - starttime)