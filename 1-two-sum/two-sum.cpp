class Solution {
public:
      vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int>ans;
        int i=0,j=n-1;
        while(i<j && j>=0){
                if (nums[i] + nums[j] == target) {
                    ans.push_back(i);
                     ans.push_back(j);
                    break;
                }
                else{
                    i++;
                }
            if(i==j){
                i=0;
                j--;
            }
            
        }
        return ans; // No solution found
    }

};