class Solution {
public:
int longestConsecutive(vector<int>& nums) {
    if(nums.size() == 0) return 0;
    sort(nums.begin(), nums.end());

    int longestSequence = 1;

    int count = 1;
    
    int i = 1;
    while(i < nums.size()){
        if(nums[i] == nums[i-1]){
            i++;       
        }
        else if(nums[i] == nums[i-1] + 1){
            count++;
            i++;
        }
        else{
            longestSequence = max(count, longestSequence);
            count = 1;
            i++;
        }  
    }
    
    longestSequence = max(count, longestSequence);
    return longestSequence;
}
};