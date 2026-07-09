class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size();
        while(nums[0]!=nums[nums[0]]){
            swap(nums[0],nums[nums[0]]);
        }
       return nums[0];
        }
};