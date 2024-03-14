package coding.implementation;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * level 2 n^2 배열 짜르기
 * 메모리 초과
 */
public class DoubleArray {
    public static void main(String[] args) {
        int n = 3;
        int left = 2;
        int right = 5;
        System.out.println(Arrays.toString(solution(n, left, right)));
    }

    public static int[] solution(int n, long left, long right) {
        int[] answer;
        int[][] doubleArray = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (i > j) {
                        doubleArray[i][j] = i + 1;
                    } else {
                        doubleArray[i][j] = j + 1;
                    }
                } else {
                    doubleArray[i][j] = i + 1;
                }

            }
        }

        List<Integer> result = new ArrayList<>();
        for (int[] array : doubleArray) {
            for (int num : array) {
                result.add(num);
            }
        }

        answer = result.stream().mapToInt(i -> i).toArray();
        return Arrays.copyOfRange(answer, Long.valueOf(left).intValue(), Long.valueOf(right + 1).intValue());
    }
}
