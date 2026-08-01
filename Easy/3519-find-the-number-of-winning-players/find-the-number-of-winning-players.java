class Solution {
    public int winningPlayerCount(int n, int[][] pick) {

        int count = 0;

        for (int player = 0; player < n; player++) {

            int[] colors = new int[11];

            for (int[] p : pick) {

                if (player == p[0]) {

                    if (++colors[p[1]] > player) {
                        count++;
                        break;
                    }
                }
            }
        }

        return count;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna