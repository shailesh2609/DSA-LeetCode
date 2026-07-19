class Solution {
public:
int longestConsecutive(vector<int>& nums) {
        unordered_set<int>st;

        for(int x:nums){
            st.insert(x);
        }

        int longestSequence = 0;
        for(int x : st){
            int length = 1;
            int curr = x; 

            // Below line means : "The previous number is not in the set."
            if(st.find(x - 1) == st.end()){

                // If x the first number of a sequence : "start counting "
                while(st.find(curr + 1) != st.end()){
                    curr++;
                    length++;
                }
                longestSequence = max(length , longestSequence); 
            }
        }
    return longestSequence;
}
};