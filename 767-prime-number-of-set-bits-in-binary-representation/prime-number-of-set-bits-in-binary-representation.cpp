class Solution {
public:
bool checkPrime(int num){
    if(num == 1) return false;
    int i = 2;
    while(i < num){
        if(num % i == 0){
            return false;
        }
        else{
            i++;
        }
    }
    return true;
}
int countSetBits(int left){
    int bitCount = 0;
    while(left > 0){
        if(left % 2 == 1){
            bitCount++;
        }
        left = left / 2;
    }
    return bitCount;
}
int countPrimeSetBits(int left, int right) {
    int ans = 0;
    while(left <= right){
        if(checkPrime(countSetBits(left))){
            ans++;
            left++;
        }
        else{
            left++;
        }
    }
    return ans;
}
};