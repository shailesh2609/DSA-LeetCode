class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int n = timePoints.size();
        vector<int> minutes(n);

        // Convert times to minutes
        for(int i=0; i<n; i++){
            int s = (stoi(timePoints[i].substr(0,2))*60) + (stoi(timePoints[i].substr(3,2)));
            minutes[i] = s ;
        }
        
        // Sort times in ascending order
        sort(minutes.begin(),minutes.end());

        // Find minimum difference across adjacent elements
        int minDiff = INT_MAX;
        for(int i=0; i < n-1; i++ ){
            minDiff = min(minDiff, minutes[i + 1] - minutes[i]);
        }

        // Consider the circular difference between first element
        minDiff = min(minDiff, 1440 - minutes.back() + minutes.front());

        return minDiff;  
}
};