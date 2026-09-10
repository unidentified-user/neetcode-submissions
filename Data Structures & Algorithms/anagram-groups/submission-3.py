class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        for string in strs:
            string_sorted = ''.join(sorted(string))
            if not anagrams_map.get(string_sorted):
                anagrams_map.update({string_sorted:[string]})
            else:
                anagrams_map[string_sorted].append(string)
        return list(anagrams_map.values())

