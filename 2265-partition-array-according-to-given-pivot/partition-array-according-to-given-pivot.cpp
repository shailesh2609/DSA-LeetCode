class Solution {
public:
     vector<int> pivotArray(vector<int>& nums, int pivot) {
    vector<int>ans;
    vector<int>smaller;
    vector<int>greater;
    int noOfPivot = 0;
    for (int i = 0; i < nums.size(); i++){
        if(nums[i] < pivot){
            smaller.push_back(nums[i]);
        }
        else if(nums[i] > pivot){
            greater.push_back(nums[i]);
        }
        else{
            noOfPivot ++;
        }
    }
    for(int ch:smaller){
        ans.push_back(ch);
    }
    while(noOfPivot){
        ans.push_back(pivot);
        noOfPivot--;
    }
    for(int ch:greater){
        ans.push_back(ch);
    }
    
    return ans;
}
};