class Solution {
public:
    int climbStairs(int n) {
    if(n <= 3) return n;
    int ans = 0;
    int prev1 = 2;
    int prev2 = 3;
    for(int i = 4; i <= n; i++){
        ans = prev1 + prev2;
        prev1 = prev2;
        prev2 = ans;
    }
    return ans;
    }
};