class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
    vector<int>ans;
    bool numsSet[101] = {false};
    int min = INT_MAX;
    int max = INT_MIN;
    for(int i=0; i < nums.size(); i++){
        numsSet[nums[i]] = true;
        if(nums[i] < min){
            min = nums[i];
        }
        if(nums[i] > max){
            max = nums[i];
        }
    } 
    for(int i = min; i <= max ; i++){
        if(numsSet[i] != true){
            ans.push_back(i);
        }
    }
    return ans;
}
};