package Stack;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class MinStack {
    // Creating a stack of list of integers.
    private Stack<List<Integer>> st;
    private List<Integer> newComb;
    public MinStack() {
        st = new Stack<>();
    }
    
    public void push(int val) {
        newComb = new ArrayList<>();
        if(st.size() < 1){
            newComb.add(val); // [val, val]
            newComb.add(val);
        }
        else{
            newComb.add(val);
            newComb.add(Math.min(val, getMin()));
        }
        st.add(newComb);
        return;

    }
    
    public void pop() {
        st.pop();
    }
    
    public int top() {
        return st.peek().get(0);
    }
    
    public int getMin() {
        return st.peek().get(1);
    }
}
