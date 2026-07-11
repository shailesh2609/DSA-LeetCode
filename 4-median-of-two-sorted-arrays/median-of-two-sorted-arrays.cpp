class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<int>nums;
    for(int ch : nums1){
        nums.push_back(ch);
    }
    for(int ch : nums2){
        nums.push_back(ch);
    }

    sort(nums.begin(), nums.end());
    int n = nums.size();
    if(n % 2 == 0){
        return (nums[(n/2)-1] + nums[n/2])/2.0;
    }
    
    return nums[n/2];   
}
};