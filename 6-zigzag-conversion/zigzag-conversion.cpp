class Solution {
public:
    string convert(string s, int numRows) {
    string ans = "";

    if(numRows == 1){
        return s;
    }

    int cycle = 2 * (numRows - 1);

    for (int i = 0; i < numRows; i++) {

        for (int j = i; j < s.length(); j += cycle) {

            // Vertical character
            ans.push_back(s[j]);

            // Diagonal character (not for first and last row)
            int diag = j + cycle - 2 * i;

            if (i != 0 && i != numRows - 1 &&
                diag < s.length()) {
                ans.push_back(s[diag]);
            }
        }

    }
    return ans;

}
};