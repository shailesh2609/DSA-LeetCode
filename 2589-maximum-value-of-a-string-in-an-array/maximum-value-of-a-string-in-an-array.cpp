class Solution {
public:
    int maximumValue(vector<string>& strs) {
    int maximum = INT_MIN;
    
    for(string ch: strs){
        bool numeric = true;

        for(char c: ch){
            if(!isdigit(c)){
                numeric = false;
                break;
            }
        }
        if(numeric){
            maximum = max( stoi(ch), maximum);
        }
        else{
            maximum = max((int)ch.length(), maximum);
        }
    }
    return maximum;
}
};