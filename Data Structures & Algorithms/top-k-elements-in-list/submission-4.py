class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter + most_common
        count = Counter(nums)
        return [item for item, _ in count.most_common(k)]