class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        result = frequency.most_common(k)
        return [m for m,n in result]