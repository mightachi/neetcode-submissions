class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_map = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            index_map[key].append(str)
        return list(index_map.values())


        