class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    int freq[128] = {0};
    int count = 0;

    int i=0;
    for(int j=0; j <s.size(); j++){
        freq[s[j]]++;

        while(freq[s[j]] > 1){
            freq[s[i]]--;
            i++;
        }

        count = max(count, j-i+1);
    }
    return count;
}

};