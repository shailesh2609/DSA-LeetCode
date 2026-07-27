class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int count = 0;

    for(int i=0; i< nums.size()- 1; i++) {
        for(int j= i+1; j < nums.size(); j++) {
            if(nums[j] + nums[i] < target){
                count ++; 
            }
            else{
                break;
            }
        }
    } 
    return count;
}
};