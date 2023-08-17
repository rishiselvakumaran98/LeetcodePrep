package Arrays_Hashing;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        // Setup an array to characters int array to hold the characters position
        int[] characters = new int[26];
        for (char a: s.toCharArray()){
            characters[a-'a']++;
        }
        for (char b: t.toCharArray()){
            characters[b-'a']--;
        }
        for (int i: characters){
            if (i != 0){
                return false;
            }
        }
        return true;
    }
}
