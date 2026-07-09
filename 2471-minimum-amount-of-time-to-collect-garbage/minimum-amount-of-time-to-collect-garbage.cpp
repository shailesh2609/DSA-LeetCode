class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
    int pickP = 0;
    int pickM = 0;
    int pickG = 0;

    int travelP = 0;
    int travelM = 0;
    int travelG = 0;

    // truck last khatkkk(konse index) travel krega ....us ke le variable banao 
    int lastP = 0;
    int lastM = 0;
    int lastG = 0;

    // calculate pick time 
    for(int i=0; i< garbage.size(); i++){
        for(int j=0; j<garbage[i].length(); j++){
            char ch = garbage[i][j];

            if(ch == 'P'){
                pickP ++;
                lastP = i;
            }
            else if(ch == 'G'){
                pickG ++;
                lastG = i;
            }
            else{
                pickM ++;
                lastM = i;
            }
        }
    }

    // calculate travel time
    for(int i=0; i< lastP; i++){
        travelP += travel[i];
    }
    for(int i=0; i< lastG; i++){
        travelG += travel[i];
    }
    for(int i=0; i< lastM; i++){
        travelM += travel[i];
    }

    int ans = (pickP + travelP) + (pickM +travelM ) + (pickG + travelG);
    return ans;
}
};