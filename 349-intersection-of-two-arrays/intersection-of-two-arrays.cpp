class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        vector<int> ans;

        unordered_map<int, int> mp1;
        unordered_map<int, int> mp2;

        for(auto num : nums1) {
            mp1[num]++;
        }

        for(auto num : nums2) {
            mp2[num]++;
        }

        for(auto num : mp1) {
            if(mp2.find(num.first) != mp2.end()) {
                ans.push_back(num.first);
            }
        }

        return ans;
    }
};