import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the commonChild function below.
    static int commonChild(String s1, String s2) {
        int x = s1.length(), y = s2.length();
        int[][] lcsMatrix = new int[x+1][y+1];
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    lcsMatrix[i+1][j+1] = lcsMatrix[i][j] + 1;
                } else {
                    lcsMatrix[i+1][j+1] = Math.max(lcsMatrix[i][j+1], lcsMatrix[i+1][j]);
                }
            }
        }
        return lcsMatrix[x][y];
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s1 = scanner.nextLine();

        String s2 = scanner.nextLine();

        int result = commonChild(s1, s2);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
