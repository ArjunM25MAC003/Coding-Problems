class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a list of tuples: (number, original_index)
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        # Sort based on the numbers
        nums_with_indices.sort()
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            curr_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            
            if curr_sum == target:
                # Return the original indices stored in the tuples
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna