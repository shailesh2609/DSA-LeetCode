class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    string temp =""; 
    int j=0;
    while(j < strs[0].length()){
        for(int i=0; i < strs.size() - 1;){
            if(strs[i][j] == strs[i + 1][j]){
                i++;
            }
            else{
                return temp;
            }
        }
        temp.push_back(strs[0][j]);
        j++;
    }
    return temp;   
}
};