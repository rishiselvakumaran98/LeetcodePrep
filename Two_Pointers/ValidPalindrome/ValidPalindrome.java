package Two_Pointers;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        char left_char, right_char;
        char[] string_char = s.toLowerCase().toCharArray();
        int left = 0;
        int right = string_char.length-1;
        while (left < right){
            left_char = string_char[left];
            right_char = string_char[right];
            if(!Character.isLetterOrDigit(left_char)) {
                left++;
                continue;
            }
            if(!Character.isLetterOrDigit(right_char)) {
                right--;
                continue;
            }
            if (left_char == right_char){
                left++;
                right--;
                continue;
            }
            return false;
        }
        return true;
    }
}
