class Solution {
public:
    // int max(int n1, int n2) {
    //     if (n1 > n2) {
    //         return n1;
    //     }
    //     return n2;
    // }
    int euch_dist(vector<int>& location) {
        return location[0] * location[0] + location[1] * location[1];
    }
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int length = commands.size();
        int max_dist = 0;
        bool done = false;
        // let north be 0 deg
        int deg = 0;
        vector<int> location = {0, 0};
        for (int i = 0; i < length; i++) {
            // iterate the commands
            if (commands[i] == -2) {
                deg += 270;
                deg %= 360;
                // now deg is one of {0, 90, 180, 270}
            }  else if (commands[i] == -1) {
                deg += 90;
                deg %= 360;
            } else {
                // we are moving forward... and should check for collisions
                if (deg == 0) { // North 
                    // look in front 1 block...
                    while (commands[i] > 0) {
                        int obs = obstacles.size();
                        location[1]++;
                        done = false;
                        for (int j = 0; j < obs; j++) {
                            if (obstacles[j][0] == location[0] && obstacles[j][1] == location[1]) {
                                location[1]--;
                                done = true;
                                break;
                            }
                        }
                        if (done) {
                            break;
                        }
                        commands[i]--;
                    }
                    max_dist = max(max_dist, euch_dist(location));
                } else if (deg == 90) { // East 
                    while (commands[i] > 0) {
                        int obs = obstacles.size();
                        location[0]++;
                        done = false;
                        for (int j = 0; j < obs; j++) {
                            if (obstacles[j][0] == location[0] && obstacles[j][1] == location[1]) {
                                location[0]--;
                                break;
                            }
                        }
                        if (done) {
                            break;
                        }
                        commands[i]--;
                    }
                    
                    max_dist = max(max_dist, euch_dist(location));
                } else if (deg == 180) { // South 
                    while (commands[i] > 0) {
                        int obs = obstacles.size();
                        location[1]--;
                        done = false;
                        for (int j = 0; j < obs; j++) {
                            if (obstacles[j][0] == location[0] && obstacles[j][1] == location[1]) {
                                location[1]++;
                                break;
                            }
                        }
                        if (done) {
                            break;
                        }
                        commands[i]--;
                    }
                    max_dist = max(max_dist, euch_dist(location));
                } else { // West 
                    while (commands[i] > 0) {
                        int obs = obstacles.size();
                        location[0]--;
                        done = false;
                        for (int j = 0; j < obs; j++) {
                            if (obstacles[j][0] == location[0] && obstacles[j][1] == location[1]) {
                                location[0]++;
                                break;
                            }
                        }
                        if (done) {
                            break;
                        }
                        commands[i]--;
                    }
                    max_dist = max(max_dist, euch_dist(location));
                }
            }
        }
        return max_dist;
    }
};