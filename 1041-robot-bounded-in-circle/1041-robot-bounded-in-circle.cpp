class Solution {
public:
    bool isRobotBounded(string instructions) {
        int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0, dir = 0;
        
        for (char instruction : instructions) {
            if (instruction == 'G') {
                // Move the robot in the current direction
                x += directions[dir][0];
                y += directions[dir][1];
            } else if (instruction == 'L') {
                // Turn left (anti-clockwise)
                dir = (dir + 3) % 4;
            } else if (instruction == 'R') {
                // Turn right (clockwise)
                dir = (dir + 1) % 4;
            }
        }
        // If the robot returns to the initial position or is not facing north, it will form a circle.
        return (x == 0 && y == 0) || (dir != 0);
    }
};