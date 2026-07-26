class Solution {
public:
    int smallestNumber(int n) {
    int countSetBits = 1;
    
    while(n/2 > 0){
        countSetBits++;
        n=n/2;
    }
    
    int ans = 0;
    for(int i = 0; i < countSetBits; i++){
        ans = ans +  pow(2,i);
    }
    return ans;
}
};