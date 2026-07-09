class Solution {
public:
   string reverseOnlyLetters(string s) {
    string letters;

     // collect letters
    for(char ch:s){
        if(isalpha(ch)){
            letters = letters + ch;
        }
    }

    int k = letters.length() - 1;

    for(int i = 0; i < s.length(); i++){
        if(isalpha(s[i])){
            s[i] = letters[k];
            k--;
        }
    }
return s;
}
};