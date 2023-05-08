"""
347. Top K Frequent Elements

Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:
  1 <= nums.length <= 105
  -104 <= nums[i] <= 104
  k is in the range [1, the number of unique elements in the array].
  It is guaranteed that the answer is unique.

Approach 1:

def topKFrequent(nums, k):
    count = {}
    res = []
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for _ in range(k):
        tmax = max(count, key = count.get)
        res.append(tmax)
        count.pop(tmax)


Approach 2:

hashMap<num, countOfNum> = {1:3, 2:2, 3:2, 4:1} 'mapping the counts of numbers in nums'
        []*k
        [ []  , [4] ,  [2, 3] ,  [1]  ,  []   ,  []   ]
           0     1       2        3      4       5
        [ []  , [4] ,  [2, 3] ,  [1]  ,  []   ,  []   ]
           0     1       2        3      4       5

>>> topKFrequent([1,1,1,2,2,3], 2)
[1, 2]

>>> topKFrequent([1], 1)
[1]
"""
def topKFrequent(nums, k):
    res = []
    numsToCount = {}
    for n in nums:
        numsToCount[n] = 1 + numsToCount.get(n, 0)
    indexesAsCountOfNum = [[] for _ in range(len(nums) + 1)]
    for n, c in numsToCount.items():
        indexesAsCountOfNum[c].append(n) 
    for i in range(len(indexesAsCountOfNum) - 1, 0, -1):
        for n in indexesAsCountOfNum[i]:
            res.append(n)
            if len(res) == k: 
                return res
