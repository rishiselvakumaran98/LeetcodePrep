package Stack;

import java.util.HashMap;
import java.util.Stack;

public class ValidParenthesis {
    public boolean isValid(String s) {
        HashMap<Character, Character> openClose = new HashMap<>();
        openClose.put('[', ']');
        openClose.put('{', '}');
        openClose.put('(', ')');
        Stack<Character> stack = new Stack<>();
        for( char c: s.toCharArray()){
            if(openClose.containsKey(c)){
                stack.add(openClose.get(c));
            } else if(stack.isEmpty() || stack.pop() != c){
                return false;
            }
        }
        return stack.isEmpty();
    }
}
