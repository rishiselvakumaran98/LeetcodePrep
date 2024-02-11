package Stack.DailyTemperatures;

import java.util.Stack;
public class DailyTemperature {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> st = new Stack<>();
        int[] answer = new int[temperatures.length];
        for (int i=0; i < temperatures.length; i++){
            while(!st.isEmpty() && temperatures[i] > temperatures[st.peek()]){
                int idx = st.pop();
                answer[idx] = i-idx;
            }
            st.push(i);
        }
        return answer;
    }
}
