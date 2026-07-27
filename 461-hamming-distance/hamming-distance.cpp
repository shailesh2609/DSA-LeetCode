class Solution {
public:
    int hammingDistance(int x, int y) {
    int ans = 0;
    int z = x^y;
    while(z){
        if(z % 2 == 1){
            ans++;
        }
        z /= 2;
    }
    return ans;
}
};