class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement][-1], i]
            index_map[num].append(i)