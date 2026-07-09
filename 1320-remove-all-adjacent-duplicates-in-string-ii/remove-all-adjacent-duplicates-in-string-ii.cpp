class Solution {
public:
    string removeDuplicates(string s, int k){
    int n = s.size();
    vector<int>count(n);

    int i=0,j=0;
    while(j < n){
        s[i] = s[j];    // --> 1
        count[i] = 1;    // --> 2

        if(i> 0 && s[i] == s[i-1]){
            count[i] += count[i-1];
        }
        if(count[i] == k){
            i -= k;
        }
        i++;
        j++;
    }
    return s.substr(0,i);
}
};