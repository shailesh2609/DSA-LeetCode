class Solution {
public:
    double slidewindow(vector<int>& nums, int k) {
    int n=nums.size();
    int i=0;
    int j=k-1;
    int sum=0;
     for(int y=i;y<=j;y++){
            sum+=nums[y];
     }
            int maxSum=sum;
            j++;
      while(j<n){
         sum-=nums[i++];
         sum+=nums[j++];
         maxSum=max(maxSum,sum);
       }   
     double maxAvg=maxSum/(double)k;
     return maxAvg;
     }
      double findMaxAverage(vector<int>& nums, int k) {
        return slidewindow(nums,k);
    }
};