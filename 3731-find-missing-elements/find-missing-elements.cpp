class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
    vector<int>ans;
    sort(nums.begin(), nums.end());

    int index = 0;
    for(int i = nums[0]; i < nums[nums.size() - 1] ; i++){
        if(i == nums[index]){
            index++;
        }
        else{
            ans.push_back(i);    
        }
    }
    return ans;
}
};