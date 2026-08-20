class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A=([nums[0]], [nums[1]])
        for x in nums[2:]:
            A[A[0][-1]<=A[1][-1]].append(x)
        return A[0]+A[1]        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna