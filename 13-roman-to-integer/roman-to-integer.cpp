class Solution {
public:
    int checkRoman(char ch){
    if(ch == 'M') return 1000;
    if(ch == 'D') return 500;
    if(ch == 'C') return 100;
    if(ch == 'L') return 50;
    if(ch == 'X') return 10;
    if(ch == 'V') return 5;
    return 1;
}
int romanToInt(string s) {
    int ans = 0;
    for(int i = 0; i < s.size(); i++){
        if(i+1 < s.size() && checkRoman(s[i]) < checkRoman(s[i+1])){
            ans -= checkRoman(s[i]);
        }
        else{
            ans += checkRoman(s[i]);
        }
    }
    return ans;
}
};