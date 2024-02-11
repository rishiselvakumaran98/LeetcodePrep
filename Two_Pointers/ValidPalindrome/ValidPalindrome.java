package Two_Pointers;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int l =0, r = s.length()-1;
        while (l <= r){
            // if the left character is not alphanumeric then increment left
            if (!Character.isLetterOrDigit(s.charAt(l))){
                l++;
                continue;
            }
            // if the right character is not alphanumeric then decrement right
            if (!Character.isLetterOrDigit(s.charAt(r))){
                r--;
                continue;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }
            l++; r--;
        }
        return true;
    }
}
