class Solution {
public:
   int peakIndexInMountainArray(vector<int>&arr){
    int n=arr.size();
    int s=0;
    int e=n-1;
    int mid=s+(e-s)/2;    
    int ans=-1;
    while(s<e){
        if(arr[mid]<arr[mid+1]){
            // Awali line hu
            // Peak right me exist krti hai
            s=mid+1;
        }
        else {
            // yaa toh me B line pr hu
            // yaa toh me peak element pr hu
            e=mid;     //--> peak element bhi lost nhi hoga or left me bhi chle gye honge
        }
        
        // mid update --> most imp
        mid=s+(e-s)/2;
    }
    return s;
}
};