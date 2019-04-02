import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    
    public static String isBalanced(String exp) {
        Stack brackets = new Stack();
        char[] charExp = exp.toCharArray();
        for (char c : charExp) {
            if (c == '(' || c == '[' || c == '{') brackets.push(c);
            else if (brackets.isEmpty()) return "NO";
            else if ((c == ']' && (char)brackets.peek() == '[') ||
                     (c == ')' && (char)brackets.peek() == '(') ||
                     (c == '}' && (char)brackets.peek() == '{')) brackets.pop();
            else return "NO";
        }
        return brackets.isEmpty() ? "YES" : "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String expression = scanner.nextLine();
            System.out.println(isBalanced(expression));
        }

        scanner.close();
    }
}
