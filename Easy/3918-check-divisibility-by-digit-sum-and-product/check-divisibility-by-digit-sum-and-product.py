class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p, x=0, 1, n
        while x>0:
            x, r=divmod(x, 10)
            s+=r
            p*=r
        return n%(s+p)==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna