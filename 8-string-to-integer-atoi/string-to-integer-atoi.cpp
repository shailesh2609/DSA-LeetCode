class Solution {
public:
   int myAtoi(string s) {
    int n = s.size();

    int i = 0;

    // leading space
    while(i<n && s[i] == ' ')
        i++;  

    // Handle empty string after spaces
    if(i == n)
        return 0;
    
    // Handle sign
    int sign = 1;
    if (s[i] == '+' || s[i] == '-') {
        if (s[i] == '-'){
            sign = -1;
        }  
        i++;
    }

    long long ans = 0;

    // Read digits
    while(i<n && isdigit(s[i])){
        ans = ans*10 + (s[i] - '0');

        // Overflow check
        if (sign == 1 && ans > INT_MAX)
            return INT_MAX;

        if (sign == -1 && -ans < INT_MIN)
            return INT_MIN;

        i++;     
    }
            
    return sign*ans;

}
};