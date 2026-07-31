class Solution {
    public int minimumPushes(String word) {
        int[] freq = new int[26];
        for (char c : word.toCharArray()) 
            freq[c - 'a']++;
        
        Arrays.sort(freq);
        int ans = 0;
        for (int i = 25; i >= 0 && freq[i] > 0; i--) 
            ans += freq[i] * ((25 - i) / 8 + 1);
        
        return ans;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna