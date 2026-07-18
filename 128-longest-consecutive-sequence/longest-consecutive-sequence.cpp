class Solution {
public:
int longestConsecutive(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    int longestSequence = 0;

    int count = 1;
    
    int i = 0;
    int j = 1;
    while(j < nums.size()){
        if(nums[i] == nums[j]){
            i++;
            j++;
        }
        else if(nums[j] == nums[i] + 1){
            count++;
            i++;
            j++;
        }
        else{
            longestSequence = max(count, longestSequence);
            count = 1;
            i++;
            j++;
        }
    }
    if(j == nums.size()){
        longestSequence = max(count, longestSequence);
    }
    return longestSequence;
}
};