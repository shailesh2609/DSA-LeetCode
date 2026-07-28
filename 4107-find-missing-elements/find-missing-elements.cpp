class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
         int n = nums.size();
         unordered_set<int>st;
         vector<int> ans;
         for(int i =0 ; i<n ; i++){
             st.insert( nums[i]);
         }
        int min = *min_element(nums.begin(), nums.end());
        int max = *max_element(nums.begin(), nums.end());
        
        while(min <= max ){
             if(st.find(min) == st.end()){
                   ans.push_back(min);
             }
            min++;
        }
       return ans;
  }
};
   