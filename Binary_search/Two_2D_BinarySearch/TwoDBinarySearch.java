package Binary_search;

public class TwoDBinarySearch {
    public boolean searchMatrix(int[][] matrix, int target) {
        // first find the target row 
        int row =  binarySearchRow(matrix, target);
        if (row == -1) return false;
        // After finding the target row, then use it to find the element index
        int col = binarySearchCol(matrix, row, target);
        return (col != -1);

    }

    public int binarySearchRow(int[][] matrix, int target){
        int l = 0;
        int r = matrix.length-1;
        int lastIndex = matrix[0].length-1;
        while(l <= r){
            int mid = l + (r-l)/2;
            if(matrix[mid][0] <= target && target <= matrix[mid][lastIndex]){
                return mid;
            }
            else if (target > matrix[mid][lastIndex]){
                l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return -1;
    }
    public int binarySearchCol(int[][] matrix, int row, int target){
        int l = 0;
        int r = matrix[0].length-1;
        while(l <= r){
            int mid = l + (r-l)/2;
            if(matrix[row][mid] < target){
                l = mid+1;
            }
            else if (matrix[row][mid] > target){
                r = mid-1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
