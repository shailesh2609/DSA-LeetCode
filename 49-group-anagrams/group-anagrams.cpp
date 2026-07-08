class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    
    map<string, vector<string> >mp;

    for(auto str:strs){
        string s = str;
        sort(s.begin(), s.end());
        mp[s].push_back(str); 
    }

    vector<vector<string>> anagrams;
    for(auto it = mp.begin(); it != mp.end(); it++){
        anagrams.push_back(it->second);
    }
    return anagrams;
}
};