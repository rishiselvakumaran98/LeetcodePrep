package Sorting;
import java.util.Arrays;
// Merge sort is implemented using a divide and conquer algorithm 
// Time complexity = 0(nlogn)
// Space complexity = O(n)
public class MergeSort {
    // overloaded methods that helps to merge array and sort them using the mergeHalves function
    public static void mergeSort(int[] arr, int[] temp, int leftStart, int rightEnd){
        if (leftStart < rightEnd){
            int mid = (leftStart+rightEnd)/2;
            mergeSort(arr, temp, leftStart, mid);
            mergeSort(arr, temp, mid+1, rightEnd);
            mergeHalves(arr, temp, leftStart, rightEnd);
        }
    }

    public static void mergeHalves(int[] arr, int[] temp, int leftStart, int rightEnd){
        int leftEnd = (leftStart+rightEnd)/2;
        int rightStart = leftEnd+1;
        int size = rightEnd-leftStart+1;

        // reference pointers 
        int left = leftStart;
        int right = rightStart;
        int index = leftStart;

        while(left <= leftEnd && right <= rightEnd){
            if(arr[left] <= arr[right]){
                temp[index] = arr[left];
                left++;
            } else{
                temp[index] = arr[right];
                right++;
            }
            index++;
        }
        // once the pointers like left or right goes out of bounds we need to copy over the remaining elements in the array
        // this is where we copy over the remaining elements from the arr
        /* Either left or right pointer is at the end so only one of these lines 1 or 2 will have an effect */
        /* 1 */System.arraycopy(arr, left, temp, index, leftEnd-left+1); // copy the remaining elements into left array
        /* 2 */System.arraycopy(arr, right, temp, index, rightEnd-right+1); // copy the remaining elements into right array
        // now we copy the entire temp array into the original array
        System.arraycopy(temp, leftStart, arr, leftStart, size);
    }

    // main method within class to help sort the given array
    public static void mergeSort(int[] arr){
        mergeSort(arr, new int[arr.length], 0, arr.length-1);
    }
    public static void main(String[] args) {
        int[] test1 = {3,5,34,7,9,2,1};
        MergeSort.mergeSort(test1);
        System.out.println(Arrays.toString(test1));
    }
}
