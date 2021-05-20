class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& i, vector<int>& newInterval) {
        i.push_back(newInterval);
        sort(i.begin(),i.end());
        vector<vector<int>> vect; 
        if(i.size()==1){
            return i;
        }
        sort(i.begin(), i.end());
        int a = i[0][0];
        int b = i[0][1];
        for(int j=1; j< i.size(); j++) {
            if(b >= i[j][0]) {
                b = max(b, i[j][1]);
            }
            else {
                vect.push_back({a,b});
                a = i[j][0];
                b = i[j][1];
            }
        }
        vect.push_back({a,b});
        return vect;
        
    }
};
