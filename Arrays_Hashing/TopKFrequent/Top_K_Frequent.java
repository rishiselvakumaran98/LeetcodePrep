package Arrays_Hashing;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;



public class Top_K_Frequent {
    /* 
     * Runtime: O(n)-> Avg, Worst -> O(n^2)
     * Space: O(n) -> used to store HashMap, but if its just quick select then we use O(1)
     */
    private Map<Integer, Integer> frequencyMap = new HashMap<>();
    // We need three methods:
    // 1. Partition method that helps to sort the array with the chosen pivot from the frequencyMap
    // 2. quickselect method that recursively helps to call partition on the array until the frequent elements are arranged based on frequency
    // 3. swap method to help in Partition method to swap the array elements based on their frequency order
    public int[] topKFrequent(int[] nums, int k) {
        //  build the frequencyMap with the num in nums
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0)+1);
        }
        //  Build a new array to store the unique elements
        int[] arr = new int[frequencyMap.size()];
        int i = 0;
        for(int key: frequencyMap.keySet()){
            arr[i++] = key;
        }
        int index = quickSelect(0, arr.length-1, arr, arr.length-k);
        return Arrays.copyOfRange(arr, index, arr.length);
    }
    public void swap(int l, int r, int[] nums){
        int temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
    }

    public int partitionLast(int l, int r, int[] nums){
        int pivot = r, prev = l;
        for(int i = l; i <r; i++){
            if(frequencyMap.get(nums[i]) < frequencyMap.get(nums[pivot])){
                swap(prev, i, nums);
                prev++;
            }
        }
        swap(prev, pivot, nums);
        return prev;
    }

    public int quickSelect(int l, int r, int[] nums, int k){
        int index = partitionLast(l, r, nums);
        if(index < k){
            return quickSelect(index+1, r, nums, k);
        }
        else if (index > k){
            return quickSelect(l, index-1, nums, k);
        }
        return index;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        Top_K_Frequent l = new Top_K_Frequent();
        int k = 2;
        int[] result = l.topKFrequent_BucketSort(nums, k);
        System.out.println(Arrays.toString(result));
    }


    /* ************************************************************************************************* */

    /* ************************************************************************************************* */

    /* 
     * Bucket Sorting 
     * Runtime: O(n)
     * Space: O(n+k) --> n max size of the buckets, k size of the frequencyMap
     */
    public int[] topKFrequent_BucketSort(int[] nums, int k){
        // build a frequencyMap
        // then build a arrayList with the frequency as the index to save the key from frequencyMap
        // Iterate through the arrayList and then add it to a new results array and stop the loop when the size of result == k

        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for(int num: nums){
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0)+1);
        }
        List<List<Integer>> buckets = new ArrayList<List<Integer>>();
        for(int key: frequencyMap.keySet()){
            int frequency = frequencyMap.get(key);
            if(buckets.get(frequency) == null) buckets.set(frequency, new ArrayList<>());
            buckets.get(frequency).add(key);
        }

        List<Integer> result = new ArrayList<Integer>();
        for(int i=buckets.size()-1; i >= 0; i--){
            if(buckets.get(i) != null){
                result.addAll(buckets.get(i));
            }
            if (result.size() == k) break;
        }
        return result.stream().mapToInt(a -> a).toArray(); // Convert the ArrayList to int[] array
    }

    public int[] topKFrequent_TreeMap(int[] nums, int k) {
        // First we compute the frequencies of the number in the nums array into a hashMap
        Map <Integer, Integer> freqMap = new HashMap<>();
        for (int n: nums){
            freqMap.put(n, freqMap.getOrDefault(n, 0)+1);
        }
        // Second we take the frequencies for the number and append it the number to it as freq -> number in a HashMap
        TreeMap<Integer, List<Integer>> numfreqMap = new TreeMap<>();
        // 
        for (Map.Entry<Integer, Integer> entry: freqMap.entrySet()){
            int num = entry.getKey();
            int freq = entry.getValue();
            numfreqMap.computeIfAbsent(freq, l -> new ArrayList<>()).add(num);
        }
        // Lastly sort the Array and take K elements and return the elements in an array
        List<Integer> retArr = new ArrayList<>();
        int count = 0;
        while (count < k) {
            Map.Entry<Integer, List<Integer>> entry = numfreqMap.pollLastEntry();
            if (entry == null){
                break;
            }
            for (int i: entry.getValue()){
                retArr.add(i);
                count++;
            }
            if (count == k){
                break;
            }
        }
        return retArr.stream().mapToInt(i -> i).toArray();
    }
}
