class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>>ans;
        if(nums.size() < 4) return ans;
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<nums.size() - 3; i++){
            if(i > 0 && nums[i] == nums[i-1] ) continue;

            for(int j=i+1; j< nums.size()- 2; j++){
                if(nums[j] == nums[j-1] && j-1 != i) continue;

                int k = j+1;
                int l = nums.size() - 1;

                while(k<l){
                    long long int sum =1LL * nums[i] + nums[j] + nums[k] + nums[l];

                    if(nums[k] == nums[k-1] && k-1 != j){
                        k++;
                    }
                    else if(sum == target){
                        ans.push_back({nums[i], nums[j], nums[k], nums[l]});
                        k++;
                        l--;  
                    }
                    else if(sum > target){
                        l--;
                    }
                    else{
                        k++;
                    }
                }    
            }
        }
        return ans;
    }
};