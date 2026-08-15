class Solution {
public:
    int fib(int n) {
        if(n == 0) return 0;
        int prev1 = 0;
        int prev2 = 1;
        int ans = 1;
        for(int i = 1 ; i< n; i++){
            ans = prev1 + prev2; 
            prev1 = prev2;
            prev2 = ans;
        }
    return ans;
    }
};