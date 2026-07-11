class Solution {
public:
       string removeDuplicates(string s){
       string temp = "";
       int i = 0;
       while(i < s.length()){
               if(temp.length() > 0 && s[i] == temp[temp.length() - 1]){
                   temp.pop_back();
               }
               else{
                   temp.push_back(s[i]);
               }
           i++;
       }
       return temp;
   }
};