package BackTracking;

import java.util.ArrayList;
import java.util.List;

public class GenerateParenthesis {
    private List<String> st;
    public List<String> generateParenthesis(int n) {
        // We can use back tracking to keep track of the number of open-close brackets we are creating
        // 1. if the open == close, we would return the array containing the String
        st = new ArrayList<>();
        backtrack(0, 0, new StringBuilder(), n);
        return st;
    }

    public void backtrack(int openN, int closeN, StringBuilder sb, int n){
        // 1. if the open == close == n, then we exit from the backtrack function
        if (openN == closeN && closeN == n){
            st.add(sb.toString());
            return;
        }
        // 2.If the open < n then we keep adding n until we close interface
        if(openN < n){
            sb.append("(");
            backtrack(openN+1, closeN, sb, n);
            sb.deleteCharAt(sb.length()-1); 
            // pop the last character from the string once we backtrack upwards
        }
        // 3. if the number of close is lesser than open then we add close and then backtrack again
        if(closeN < openN){
            sb.append(")");
            backtrack(openN, closeN+1, sb, n);
            sb.deleteCharAt(sb.length()-1); 
            // pop the last character from the string once we backtrack upwards
        }

    }
}
