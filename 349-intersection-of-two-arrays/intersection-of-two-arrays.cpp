class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    vector<int>ans;
    bool checkExistence[1001] = {false}; 
    for(int num:nums1){
        if(!checkExistence[num]){
            checkExistence[num] = true;
        }
    }
    for(int num:nums2){
        if(checkExistence[num]){
            ans.push_back(num);
            checkExistence[num] = false;
        }
    }
    return ans;   
}
};