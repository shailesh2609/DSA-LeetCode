class Solution {
public:
     vector<int> pivotArray(vector<int>& nums, int pivot) {
    vector<int>ans;
    int noOfPivot = 0;
    for(int ch : nums){
        if(ch < pivot){
            ans.push_back(ch);
        }
    }
    for(int ch : nums){
        if(ch == pivot){
            ans.push_back(ch);
        }
    }
    for(int ch : nums){
        if(ch > pivot){
            ans.push_back(ch);
        }
    }
    
    return ans;
}
};