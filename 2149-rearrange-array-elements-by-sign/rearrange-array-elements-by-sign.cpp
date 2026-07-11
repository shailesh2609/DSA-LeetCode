class Solution {
public:
     vector<int>rearrangeArray(vector<int>&nums){
    vector<int>ans(nums.size(),-1);
    int odd=1,even=0;
    for(int i=0;i<nums.size();i++){
        int num=nums[i];
        if(num>0){
            ans[even]=num;
            even+=2;
        }
        else{
           ans[odd]=num;
            odd+=2;
        }
    }
    return ans;
}
};