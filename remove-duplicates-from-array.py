"""
  ever-empty? N
  ever an unpexpected type? N
  # of items in input array always matches whats expected for the integer input? Y
  array only has int? Y
  no extra memory allocated? Y
  
  ( i1 : integer -1,0,1 , i2: [a,b,c,...] ) ---> function: lengthOfDistincts ---> ( o : integer)
  
  inputs: 4, [1,3,3,5]
  output: return 3             --- [1, 3, 5]
  
  input: 3, [4, 5, 6]
  output: return 3
  
  input: 1, [1]
  output: return 1
 
  
>>> lengthOfDistinctNums(4, [1,3,3,5])
True
>>> lengthOfDistinctNums(3, [4,5,6]) 
True
>>> lengthOfDistinctNums(1, [1, 1, 1, 1])
True
>>> lengthOfDistinctNums(4, [2, 7, 1, 1])
False

print(ex1, ex1 == 3)
print(ex2, ex2 == 3)   
print(ex3, ex3 == 1)    
"""
def lengthOfDistinctNums(i, nums):
        # nums -> filter to include only numbers that meet a condition (if the number's count in the array is == 1) -> len(filteredArray)
        # return len(list(filter(lambda x : if nums.contains(x) == 1, nums)))
    return len(set(nums))
    
    
    
    
    
