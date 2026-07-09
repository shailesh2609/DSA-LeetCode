class Solution {
public:
    int addDigits(int num) {
        while(num>=10){
            int n = 0;
            while(num > 0){
                n = n + num % 10;
                num = num / 10;
            }
            num = n;
        }
        return num;
    }
};