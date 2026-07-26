class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        if(nums.size() < 2 ) return true;
        int i = 0;
        while(i < nums.size() - 1){
            if((nums[i] % 2 == 0 && nums[i+1] % 2 != 0) || ( nums[i] % 2 == 1 && nums[i+1] % 2 != 1)){
                i++;
            }
            else{
                return false;
            }
        }
        return true;
    }
};