class Solution {
public:
    int missingNumber(vector<int>nums){
    int n=nums.size();
     sort(nums.begin(),nums.end());
    int s=0;
    int e=n-1;
    int mid=s+(e-s)/2;    
    while(s<=e){
        int diff=nums[mid]-mid;
        if(diff==0){
            // right me jao
            s=mid +1;
        }
        else {
           
            // left me jao
            e=mid -1;
        }
        // mid update --> most imp
        mid=s+(e-s)/2;
    }
    return s;
}
};