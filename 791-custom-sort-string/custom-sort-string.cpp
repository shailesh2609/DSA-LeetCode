class Solution {
public:
static string str;              // Global Variable
static bool compare(char char1 , char char2){

    // this will return true, if position of char1 in str string is less
    // then the position of char2 in str string

    // when true is returned, then char1 will be placed before char2 
    // in output string
    return(str.find(char1) < str.find(char2)) ;
}
string customSortString(string order, string s){
    str = order;
    sort(s.begin(), s.end(), compare);
    return s;
}
};

string Solution::str;