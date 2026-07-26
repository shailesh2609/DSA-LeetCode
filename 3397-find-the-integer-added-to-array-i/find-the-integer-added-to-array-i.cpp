class Solution {
public:
   int sum(vector<int>nums){
    int sum = 0;
    for(int ch : nums){
        sum += ch;
    }
    return sum;
}
int addedInteger(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    return (sum(nums2) - sum(nums1))/n;
}
};