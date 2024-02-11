package Binary_search.TimeKeyValueStore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javafx.util.Pair;

public class TimeMap {
    private Map<String, List<Pair<String, Integer>>> ks;
    public TimeMap() {
        // Initialize a HashMap<Int, PAIR> to keep track of the (key, value, timestamp)
        ks = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        // if key exists in the Store then replace it with value and timestamp
        List<Pair<String, Integer>> keyList = ks.containsKey(key) ? ks.get(key) : new ArrayList<>();
        keyList.add(new Pair<>(value, timestamp));
        ks.put(key, keyList);
    }
    
    public String get(String key, int timestamp) {
        if (!ks.containsKey(key)) return "";
        List<Pair<String, Integer>> keyList = ks.get(key);
        // perform binary search on the sorted key-value store
        int l = 0, r = keyList.size()-1;
        int max_m = -1;
        while (l <= r) {
            int m = l+(r-l)/2;
            if (keyList.get(m).getValue() <= timestamp){
                max_m = m;
                l = m+1;
            }
            else {
                r = m-1;
            }
        }
        return max_m != -1 ? keyList.get(max_m).getKey() : "";
    }
}
