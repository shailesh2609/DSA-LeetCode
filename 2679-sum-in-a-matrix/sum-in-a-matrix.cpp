class Solution {
public:
int matrixSum(vector<vector<int>>& nums) {
    int score = 0;

    for(int i=0; i<nums.size(); i++){
        sort(nums[i].begin(), nums[i].end());
    }
    for(int i=0; i<nums[0].size(); i++){
        int maxNum = INT_MIN;
        for(int j=0; j<nums.size(); j++){
            maxNum = max(maxNum, nums[j][i]);
        }
        score += maxNum;
    }
    return score;
}
};