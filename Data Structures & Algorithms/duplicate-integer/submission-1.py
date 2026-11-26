class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for num in nums:
            if num in frequency:
                return True
            frequency[num] = frequency.get(num,0)+1
        return False