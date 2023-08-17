package Arrays_Hashing;

import java.util.HashSet;

public class validSudoku {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> visited = new HashSet<>();
        for (int i=0;i < board.length; ++i){
            for (int j=0; j< board[0].length; ++j){
                if (board[i][j] != '.'){
                    String cell = "(" + board[i][j] + ")";
                    if (!visited.add(cell+i) || !visited.add(j+cell) || !visited.add(i/3+cell+j/3)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
