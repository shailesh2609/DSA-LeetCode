class Solution {
public:
    int smallestNumber(int n) {
    int countSetBits = 1;
    
    while(n/2 > 0){
        countSetBits++;
        n=n/2;
    }
    
    int ans = n;
    while(true){
        n = ans;
        int index = 0;
        while(n > 0){
            if(n % 2 == 1){
                index++;
            }
            n = n/2;
        }
        if(countSetBits != index){
            ans++;
            continue;
        }
        else{
            break;
        }
    }
    return ans;
}
};