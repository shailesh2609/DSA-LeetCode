class Solution {
public:
   vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        int total = row*col;

        int firstRow = 0;
        int lastRow = row-1;
        int firstCol = 0;
        int lastCol = col-1;

        int count = 0;
        vector<int> res(total);
        while (count < total) {
            for (int i=firstCol; count < total && i<=lastCol; i++) {
                res[count] = matrix[firstRow][i];
                count++;
            }
            firstRow++;

            for (int i=firstRow; count < total && i<=lastRow; i++) {
                res[count] = matrix[i][lastCol];
                count++;
            }
            lastCol--;

            for (int i=lastCol; count < total && i>=firstCol; i--) {
                res[count] = matrix[lastRow][i];
                count++;
            }
            lastRow--;

            for (int i=lastRow; count < total && i>=firstRow; i--) {
                res[count] = matrix[i][firstCol];
                count++;
            }
            firstCol++;
        }
        
        return res;
    }
};