class Solution {
public:
   bool checkPrime(int left){
       // Count the Set Bits 
       int bitCount = 0;
       while(left > 0){
           if(left % 2 == 1){
               bitCount++;
           }
           left /= 2;
       }

       // Check if it is prime or not
       if(bitCount < 2) return false;
       for(int i=2; i*i <= bitCount ; i++){
           if(bitCount % i == 0){
               return false;
           }
       }
       return true;
   }
   int countPrimeSetBits(int left, int right) {
       int ans = 0;
       while(left <= right){
           if(checkPrime(left)){
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