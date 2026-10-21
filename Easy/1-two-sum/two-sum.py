class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_with_i = [(num,i) for i, num in enumerate(nums)]
        nums_with_i.sort()

        left = 0
        right = len(nums)-1
        
        while(left < right):
            curr_sum = nums_with_i[left][0] + nums_with_i[right][0]

            if(curr_sum == target):
                return [nums_with_i[left][1] , nums_with_i[right][1]]
            elif curr_sum < target:
                left += 1
            else: 
                right -= 1
            
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna