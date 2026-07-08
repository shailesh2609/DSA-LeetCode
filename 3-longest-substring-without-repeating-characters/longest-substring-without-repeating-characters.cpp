class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    vector<int>freq(128,-1);
    int maxLength = 0;

    int i=0;
    for(int j=0; j < s.size(); j++){
        if (freq[s[j]] >= i) {
                i = freq[s[j]] + 1;
            }
            freq[s[j]] = j;
            maxLength = max(maxLength, j - i + 1);
    }
    return maxLength;
}
};