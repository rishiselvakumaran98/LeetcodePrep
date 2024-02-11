package Stack.LargestRectangle;

import java.util.Stack;
import javafx.util.Pair;

public class LargestRectangle {
    public int largestRectangleArea(int[] heights) { 
        int maxArea = 0;
        Stack<Pair<Integer, Integer>> st = new Stack<>(); // to store the (i, height)
        for (int i=0; i < heights.length; i++){
            int start = i;
            while (!st.isEmpty() && st.peek().getValue() > heights[i]){
                Pair<Integer, Integer> rectCell = st.pop();
                int idx = rectCell.getKey();
                int area = rectCell.getValue() * (i - idx);
                maxArea = Math.max(maxArea, area);
                start = idx;
            }
            st.push(new Pair<> (start, heights[i]));
        }
        
         while (st.size() > 0){
            Pair<Integer, Integer> cell = st.pop();
            maxArea = Math.max(maxArea, cell.getValue() * (heights.length - cell.getKey()));
         }
         return maxArea;
    }
}
