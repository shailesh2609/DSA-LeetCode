class Solution {
public:
    string reorganizeString(string s) {
    int freq[26] = {0};

    for(int i = 0; i < s.length(); i++){
            freq[s[i] - 'a']++;
    }

    // find the most frequent (occurrent) character
    int maxFreq = INT_MIN;
    char mostFreqChar;
    for(int i = 0; i < 26 ; i++){
        if(freq[i] > maxFreq){
            maxFreq = freq[i];
            mostFreqChar = 'a' + i;
        } 
    }

    int index = 0;
    while(maxFreq > 0 && index < s.length()){
        s[index] = mostFreqChar;
        maxFreq--;
        index += 2;
    }

    if(maxFreq != 0){
        return "";
    }

    freq[mostFreqChar - 'a'] = 0;

    // let's place the rest of the characters
    for(int i = 0; i< 26; i++){
        while(freq[i] > 0){
            index = index >= s.length() ? 1 : index;
            s[index] = i + 'a';
            freq[i]--;
            index += 2; 
        }
    }
    return s;
}
};