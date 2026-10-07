class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive solution – O(n^2)
        output = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    output[i] *= nums[j]

        return output
