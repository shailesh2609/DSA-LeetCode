class Solution {
public:
     string intToRoman(int num) {
        string romanSymbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9 , 5, 4, 1};

        string ans = "";
        int i=0;
        while(num > 0){
            if(num >= values[i]){
                ans += romanSymbols[i];
                num -= values[i];
            }
            else{
                i++;
            }
        }
        return ans;
    }
};