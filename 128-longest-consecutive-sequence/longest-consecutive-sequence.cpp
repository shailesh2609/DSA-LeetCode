class Solution {
public:
int longestConsecutive(vector<int>& nums) {
    if(nums.size() == 0) return 0;
    sort(nums.begin(), nums.end());
    int seq = 1;
    int count = 0;
    int i = 0;
    int j = 1;
    while(j < nums.size()){
        if(nums[i] == nums[j]){
            i++;
            j++;
        }
        else if(nums[j] == nums[i] + 1){
            seq++;
            i++;
            j++;
        }
        else{
            count = max(seq, count);
            seq = 1;
            i++;
            j++;
        }
    }
    
        count = max(seq, count);

    return count;
}
};