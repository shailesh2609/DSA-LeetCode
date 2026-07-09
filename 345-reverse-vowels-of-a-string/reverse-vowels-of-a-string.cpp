class Solution {
public:
bool isVowels(char c){
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
       c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ){
        return true;
    }
    return false;
}
    string reverseVowels(string s) {
        int i = 0;
        int j = s.length() - 1;
        while(i < j){
            if( isVowels(s[i]) && isVowels(s[j]) ){
                swap(s[i], s[j]);
                i++;
                j--;
            }
            else if( !isVowels(s[i]) ){
                i++;
            }
            else{
                j--;
            }
        } 
        return s;
    }
};