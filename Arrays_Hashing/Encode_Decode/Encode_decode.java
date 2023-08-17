package Arrays_Hashing;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Encode_decode {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        // add hashes to each of the strings to encode their values
        StringBuilder sb = new StringBuilder();
        for(String s: strs){
            sb.append(s.length()).append("/").append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while(i < s.length()){
            int slash = s.indexOf("/", i);
            int size = Integer.parseInt(s.substring(i, slash));
            i = size+slash+1;
            result.add(s.substring(slash+1, i));
        }
        
        return result;
    }

    public static void main(String[] args) {
        String[] test = {"Hello","World"};
        List<String> strs = Arrays.asList(test);
        Encode_decode codec = new Encode_decode();
        System.out.println(codec.decode(codec.encode(strs)));

    }
}
