class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive solution
        frequencies = dict.fromkeys(nums, 0)
        
        for num in nums:
            frequencies[num] += 1
        
        top_k_frequent = sorted(frequencies, key=frequencies.get, reverse=True)[:k]
        return top_k_frequent