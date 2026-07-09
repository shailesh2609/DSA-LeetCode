class Solution {
public:
 int bs(vector<int>arr,int x){
   int s =0;
   int e =arr.size()-1;
   int ans=e;
   
   while(s<=e){
      int mid =s+(e-s)/2;
      if(arr[mid] >= x){
         ans=mid;
         e=mid-1;
      }
      else{
         s=mid+1;
      }
   }
   return ans;
}


vector<int> findClosestElements(vector<int>& arr, int k, int x) {
   int n = arr.size();
   int h = bs(arr,x);
   int l= h-1;

   while(k--){
      if(l<0){
           h++;
      }
      else if(h>=arr.size()){
         l--;
      }
      else if(x-arr[l]>arr[h]-x){
        h++;
      }
      else{
         l--;
      }
   }
   
   return vector<int>(arr.begin()+l+1,arr.begin()+h);    
}
};