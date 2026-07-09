class Solution {
public:
    int expand (string s , int i , int j){
    int n= s.length();
    int count = 0;
    while(i >= 0 && j < n && s[i] == s[j]){
        count ++;
        i--;
        j++;
    } 
    return count;
}
int countSubstrings(string s) {
    int n = s.length();
    int totalCount = 0; 

     
    for(int center = 0; center < n; center++ ) {
    // For ODD palindromic substrings
        int oddKaAns = expand(s, center, center);

    // For EVEN palindromic substrings
        int evenKaAns = expand(s, center, center+1);

        totalCount = totalCount + oddKaAns+ evenKaAns;
    }
    return totalCount;
}
};