class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int num = x;
        while(num){
            sum += num % 10 ;
            num /= 10;
        }
        if(x % sum == 0){
            return sum;
        }
        return -1;
    }
};