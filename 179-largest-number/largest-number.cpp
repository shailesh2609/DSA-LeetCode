class Solution {
public:
static bool compare(const string &a , const string &b){
    string t1 = a + b;
    string t2 = b + a;
    return t1 > t2;
}
string largestNumber(vector<int>& nums) {
    // edge case:- nums =[0,0]
    int count = 0;   // for edge case we will take count 

    vector<string>strNums;
    for(int x:nums){
        if(x != 0){
            strNums.push_back(to_string(x));   
        }
        else{
            strNums.push_back(to_string(x)); 
            count ++;
        } 
    }
    // simply is count is equal to size of vector --> return "0"  HENCE EDGE CASE HANDLED
    if(count == nums.size()){
        return "0";
    }

    sort(strNums.begin(), strNums.end(), compare);

    string ans="";
    int i=0;
    while (i<strNums.size()){
        ans += strNums[i];
        i++;
    }
    return ans;
}
};