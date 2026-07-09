class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string u="";
        string v="";
        long long int i=0;
        long long int j=0;
        while(i<s.length()){
            if(s[i] != '#' ){
                u.push_back(s[i]);
            }
            else if(u != ""){
                u.pop_back();
            }
            i++;
        } 
        while(j<t.length()){
            if(t[j] != '#' ){
                v.push_back(t[j]);
            }
            else if(v != ""){
                v.pop_back();
            }
            j++;
        }
        if(u == v){
                return true;
            }
            else{
                return false;
            }
        
    }
};