package programmers;

import java.util.*;
/*
* 처음에 j값을 0으로 초기화해서 정확성은 다 맞았지만 시간효율성에서 다 틀려서 85점이었다
* 그러다가 생각해보니 정렬 이후에 비교한 숫자를 다시 볼 필요가 없기에 j = i로 초기화하였고,
* 덕분에 빠르게 풀 수 있었다. 레벨 3치고는 쉬운 문제였다
* 프로그래머스 '숫자 게임' 문제, 레벨 3, 2021.11.08 */
public class NumberGame {
    public static int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        boolean[] check = new boolean[B.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = i; j < B.length; j++) {
                if (A[i] < B[j] && check[j] == false) {
                    answer += 1;
                    check[j] = true;
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] A = {5, 1, 3, 7};
        int[] B = {2, 2, 6, 8};
        System.out.println(solution(A, B));
    }
}
