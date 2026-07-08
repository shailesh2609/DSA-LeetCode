class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        //transpose
        for(int i=0; i<n; i++) {
            for(int j=i; j<matrix[i].size(); j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        //reverse -> 2D MATTIX ki ssaari rows ko 
        //kitni rows h -> 0 > (n-1)
        for(int i=0; i<n; i++) {
            //hr row ko reverse krna h 
            reverse(matrix[i].begin(),matrix[i].end()); //reverse is a utility function 
        }

        
    }
    
};