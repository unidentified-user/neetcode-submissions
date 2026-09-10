class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        abc_map = {v:k for k,v in enumerate(abc)}
        anagrams_map = {}

        for string in strs:
            key = [0] * 26
            for char in string:
                key[abc_map[char]] += 1
            anagrams_map.setdefault(tuple(key), []).append(string)
        return list(anagrams_map.values())
