package coding.sorting;

import java.util.Arrays;

/**
 * level 2 H-Index
 */
public class HIndex {
    public static void main(String[] args) {
        int[] citations = {3, 0, 6, 1, 5};
        System.out.println(solution(citations));
    }

    private static int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations); //[0, 1, 3, 5, 6]

        for (int i = 0; i < citations.length; i++) {
            int h = citations.length - i;
            if (citations[i] >= h) {
                answer = h;
                break;
            }
        }
        return answer;
    }
}
