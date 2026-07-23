class Solution {
public:
vector<int> divisibilityArray(string word, int m) {
    int n = word.size();
    vector<int>ans;

    long long rem = 0;
    for(int i = 0; i < n; i++){
        rem = rem*10 + (word[i]- '0') ;
        if(rem % m == 0){
            ans.push_back(1);
        }
        else{
            ans.push_back(0);
        } 
        rem = rem % m;
    }
    return ans;
}
};