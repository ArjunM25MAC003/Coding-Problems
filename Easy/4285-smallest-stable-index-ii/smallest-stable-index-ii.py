class Solution:
    def firstStableIndex(self, A: List[int], k: int) -> int:
        msf = -1
        cand = cm = 0

        for i, x in enumerate(A):
            msf = max(msf, x)

            if i == cand:
                cm = msf

            if x < cm - k:
                cand = i + 1

        return cand if cand < len(A) else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna