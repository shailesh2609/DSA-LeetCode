class Solution {
public:

string expand (string s, int i, int j){
    int n = s.size();
    while(i >= 0 && j < n && s[i] == s[j]){
        i--;
        j++;
    }
    
    return s.substr(i+1, j-i-1);
}
string longestPalindrome(string s) {
    string ans ="";
    
    for(int center = 0; center < s.size(); center ++){
    // For ODD palindromic substrings
        string oddKaAns = expand (s, center, center);

    // For EVEN palindromic substrings
        string evenKaAns = expand (s, center, center + 1);

        if(oddKaAns.length() > ans.length()){
            ans = oddKaAns;
        }
        if(evenKaAns.length() > ans.length()){
            ans = evenKaAns;
        }
    }   
    return ans;
}
};   