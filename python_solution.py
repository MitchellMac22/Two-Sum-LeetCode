class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Construct a hashmap
        hashmap = {}
        
        # Iterate over the array
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
