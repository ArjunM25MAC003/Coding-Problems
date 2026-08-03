class Solution {
public:
    int stoneGameVI(vector<int>& alic, vector<int>& bob) {
        int n=alic.size();
        vector<pair<int,int>>a(n);
        for(int i=0;i<n;i++){
            a[i]={alic[i],bob[i]};
        }
        sort(a.begin(),a.end(),[&](pair<int,int>&x,pair<int,int>&y){
            return x.first+x.second>y.first+y.second;
        });
        int ans1=0,ans2=0;
        for(int i=0;i<n;i++){
            if(i&1){
                ans2+=a[i].second;
            }
            else{
                ans1+=a[i].first;
            }
        }
        if(ans1<ans2) return -1;
        if(ans2<ans1) return 1;
        return 0;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna