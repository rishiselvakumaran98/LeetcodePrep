package Heaps.DesignHeap;

import java.util.Arrays;

public class MinInHeap{
    private int capacity = 10;
    private int size = 0;

    private int[] items = new int[capacity];
    
    // Method to get the leftChildIndex
    private int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
    private int getRightChildIndex(int parentIndex) { return 2* parentIndex + 2; }
    private int getParentIndex(int childIndex) { return (childIndex-1) /2; }


    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < size; }
    private boolean hasParent(int index) { return getParentIndex(index) >= 0; }

    private int getLeftChild(int index) { return items[getLeftChildIndex(index)]; }
    private int getRightChild(int index) { return items[getRightChildIndex(index)]; }
    private int getParent(int index){ return items[getParentIndex(index)]; }

    // We need to add two more extra methods
    private void swap(int index1, int index2){
        int temp = items[index1];
        items[index1] = items[index2];
        items[index2] = temp;
    }

    private void ensureExtraCapacity(){
        if (size == capacity){
            items = Arrays.copyOf(items, capacity*2);
            capacity *= 2;
        }
    }

    // Implement a peek method that helps check the min element
    public int peek() throws IllegalStateException {
        if (size == 0) throw new IllegalStateException();
        return items[0];
    }

    // Checks for the first element and removes and returns it from the array
    public int poll() throws IllegalStateException {
        if (size == 0) throw new IllegalStateException();
        int item = items[0];
        items[0] = items[size-1];
        size--;
        heapifyDown(); // fix each element swapping with its child node as necessary
        return item;
    }

    public void add(int num){
        ensureExtraCapacity();
        items[size] = num;
        size++;
        heapifyUp(); // fix each element swapping with its parent node as necessary
    }

    public void heapifyDown(){
        int index = size-1;
        // Walk up as long as there is a parent item and as long as I am out of order
        while (hasParent(index) && getParent(index) > items[index]){ // parent element should be smaller than child as its MinHeap
            swap(getParentIndex(index), index);
            // Walk upwards
            index = getParentIndex(index);
        }

    }

    public void heapifyUp(){
        int index = 0;
        // Fix the left child as without the left child there is no right child ( As heaps are balanced)
        while (hasLeftChild(index)){
            int smallerChildIndex = getLeftChildIndex(index);
            if (hasRightChild(index) && getRightChild(index) < getLeftChild(index)){ // right child should be > leftChild
                smallerChildIndex = getRightChildIndex(index);
            }
            //  We are looking downwards on the heap
            // If the current index is smaller than the smallest of the two children then we are good
            if (items[index] < items[smallerChildIndex]){
                break;
            } else {
                // If its not true then we swap it and move down to the smaller child
                swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
            
        }
    }
}