class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        L1=[(i<<10)+j for i, row in enumerate(img1) for j, c in enumerate(row) if c==1]
        L2=[(i<<10)+j for i, row in enumerate(img2) for j, c in enumerate(row) if c==1]
        diff=defaultdict(int)
        for x in L1:
            for y in L2:
                diff[x-y]+=1
        return max(diff.values(), default=0)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna