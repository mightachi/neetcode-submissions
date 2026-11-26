class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count[num]                 # Frequency of num
        count.items()              # (element, frequency)
        count.keys()               # Unique elements
        count.values()             # Frequencies
        count.most_common(1)       # Most frequent
        # Sort by first element
        arr.sort(key=lambda x: x[0])

        # Sort by second element
        arr.sort(key=lambda x: x[1])

        # Sort by first, then second
        arr.sort(key=lambda x: (x[0], x[1]))

        # Sort by second, then first
        arr.sort(key=lambda x: (x[1], x[0]))

        # Descending order by first element
        arr.sort(key=lambda x: x[0], reverse=True)

        # Create a new sorted list
        new_arr = sorted(arr, key=lambda x: x[0])
        """
        frequency = Counter(nums)
        result = frequency.most_common(k)
        return [m for m,n in result]