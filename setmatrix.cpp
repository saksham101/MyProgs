class Solution {
public:
    void setZeroes(vector<vector<int>>& mat) {
        int row_len = mat.size();
        int col_len = mat[0].size();
        set <int> row;
        set <int> col;
        
        for(int i = 0; i < row_len; i ++) {
            for(int j = 0; j < col_len; j ++) {
                if(mat[i][j] == 0) {
                    row.insert(i);
                    col.insert(j);
                }
            }
        }
        
        for(auto i = row.begin(); i != row.end(); ++i) {
            for(int j = 0; j < col_len; j ++) {
                mat[*i][j] = 0;
            }
        }
        
        for(auto i = col.begin(); i != col.end(); ++i) {
            for(int j = 0; j < row_len; j ++) {
                mat[j][*i] = 0;
            }
        }
        
        // return mat;
    }
};
