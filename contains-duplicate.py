""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if 
every element is distinct.

Example 1
>>> containsDuplicate([1,2,3,1])
True

Example 2
>>> containsDuplicate([1,2,3,4])
False

Example3
>>> containsDuplicate([1,1,1,3,3,4,3,2,4,2])
True
"""

def containsDuplicate(nums):
  numbersSeen = set()
  for n in nums:
    if n in numbersSeen:
      return True
    numbersSeen.add(n)
  return False

