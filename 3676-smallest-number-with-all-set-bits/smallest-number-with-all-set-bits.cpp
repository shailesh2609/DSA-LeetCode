class Solution {
public:
    int smallestNumber(int n) {
        int ans = -1;

        int index = 0;
        int  num = n;
        while(num != 0){
            num = num >> 1;
            index++;
            if(index == 1) ans = 2;
            else ans*=2;
        }
    return ans-1;
}
};