package Stack.CarFleet;

import java.util.Arrays;

public class CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        // Zip the arrays into a 2D array, then sort it based on the position of the cars closest to the target
        int n = position.length;
        double [][] zipArr = new double[n][2];
        for (int i=0; i < n; i++){
            zipArr[i][0] = position[i];
            zipArr[i][1] = (double) (target-position[i])/speed[i]; // time taken to reach target
        }
        // Sort the Array based in its position from Target
        Arrays.sort(zipArr, (a,b) -> Double.compare(a[0], b[0]));
        // Iterate from largest pos to smallest in reverse
        int carFleet = 0; 
        double currTime = 0;
        for(int i=n-1; i>=0; i--){
            if (zipArr[i][1] > currTime){
                carFleet++;
                currTime = zipArr[i][1];
            }
        }
        return carFleet;
    }
}
