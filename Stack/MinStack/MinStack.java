package Stack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class MinStack {
    // Creating a stack of list of integers.
    public Stack<List<Integer>> st;
    public MinStack() {
        st = new Stack<>();
    }
    
    public void push(int val) {
        if (st.isEmpty()){
            st.push(Arrays.asList(val, val));
        } else {
            int minVal = Math.min(st.peek().get(0), val);
            st.push(Arrays.asList(minVal, val));
        }
    }
    
    public void pop() {
        st.pop();
    }
    
    public int top() {
        return st.peek().get(1);
    }
    
    public int getMin() {
        return st.peek().get(0);
    }
}

class MinStack2 {
    // Creating a stack of list of integers.
    public Node head;
    public MinStack2() {
        
    }
    
    public void push(int val) {
        if (head == null){
            head = new Node(val, val, null);
        } else {
            head = new Node(Math.min(head.minVal, val), val, head);
        }
    }
    
    public void pop() {
        head = head.next;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.minVal;
    }

    private class Node {
        int val;
        int minVal;
        Node next;

        private Node(int minVal, int val, Node next){
            this.val = val;
            this.minVal = minVal;
            this.next = next;
        }
    }
}
