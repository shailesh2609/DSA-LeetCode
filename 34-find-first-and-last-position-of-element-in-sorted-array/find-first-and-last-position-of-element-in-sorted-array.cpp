class Solution {
public:

int firstOccurence(vector<int> arr,int target){
    int n=arr.size();
    int s=0;
    int e=n-1;
    int mid=s+(e-s)/2;    
    int ans=-1;
    while(s<=e){
        if(arr[mid]==target){
            // ans store
            ans=mid;
            e=mid-1;
        }
        else if(target>arr[mid]){
            // right me jao
            s=mid +1;
        }
        else if(target<arr[mid]){
            // left me jao
            e=mid -1;
        }
        // mid update --> most imp
        mid=(s+e)/2;
    }
    return ans;
}

int lastOccurence(vector<int> arr,int target){
    int n=arr.size();
    int s=0;
    int e=n-1;
    int mid=s+(e-s)/2;    
    int ans=-1;
    while(s<=e){
        if(arr[mid]==target){
            // ans store
            ans=mid;
            s=mid+1;
        }
        else if(target>arr[mid]){
            // right me jao
            s=mid +1;
        }
        else if(target<arr[mid]){
            // left me jao
            e=mid -1;
        }
        // mid update --> most imp
        mid=(s+e)/2;
    }
    return ans;
}

    vector<int> searchRange(vector<int>& arr, int target) {
    int firstOcc= firstOccurence(arr ,target);
    int lastOcc= lastOccurence(arr,target);
    return{firstOcc,lastOcc};
    }
};