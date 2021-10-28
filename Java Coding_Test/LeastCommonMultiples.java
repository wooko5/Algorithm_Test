package test;

import java.util.*;

class LeastCommonMultiples {
    public int calculateLcm(int number1, int number2) {
        for (int i = Math.max(number1, number2); i < number1 * number2; i++) {
            if (i % number1 == 0 && i % number2 == 0) {
                return i;
            }
        }
        return number1 * number2;
    }

    public int solution(int[] arr) {
        int temp;
        Arrays.sort(arr);
        int answer = arr[0];

        for (int i = 0; i < arr.length - 1; i++) {
            temp = calculateLcm(answer, arr[i + 1]);
            answer = temp;
        }

        return answer;
    }
}
