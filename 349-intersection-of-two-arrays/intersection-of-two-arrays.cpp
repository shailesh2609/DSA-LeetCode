class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    vector<int>ans;
    unordered_set<int>st1;
    unordered_set<int>st2;
    for(int num:nums1){
        st1.insert(num);
    } 
    for(int num:nums2){
        st2.insert(num);
    } 
    for(int num:st1){
        if(st2.find(num) != st2.end()){
            ans.push_back(num);
        }
    }   
    return ans;       
}
};