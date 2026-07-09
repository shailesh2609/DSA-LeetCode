class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector <int> ans;
        while(left <= right){
            int k = left;
            bool ok = true;
            while(k > 0){
                int l = k % 10;

                if(l == 0 || left % l != 0 ){
                    ok = false;
                    break;
                }
                k = k / 10;
            }
            if (ok){
                ans.push_back(left);
            }
            left++;
        }
        return ans;
    }
};