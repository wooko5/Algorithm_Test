package programmers;

import java.util.*;

/*
 * dp에 잼병이기 때문에 소스코드를 보고 풀었다. 확실히 dp는 점화식을 세우는게 관건인 것 같다
 * dp와 dfs/bfs 문제를 더 많이 풀어볼까 생각중이다.
 * 프로그래머스 '스티커 모으기' 문제, 레벨 3, 2021.11.08 */
public class Sticker {
    private int[] dp1, dp2;
    private int[] array;

    public int solution(int sticker[]) {
        dp1 = new int[sticker.length];
        dp2 = new int[sticker.length];
        this.array = sticker.clone();
        dp1[0] = sticker[0];
        sticker[sticker.length - 1] = 0;

        if (sticker.length == 1) {
            return sticker[0];
        }

        for (int i = 1; i < sticker.length; i++) {
            if (i == 1) {
                dp1[i] = sticker[i];
                dp2[i] = array[i];
            } else if (i == 2) {
                dp1[i] = sticker[i] + dp1[0];
                dp2[i] = array[i] + dp2[0];
            } else {
                dp1[i] = sticker[i] + Math.max(dp1[i - 2], dp1[i - 3]);
                dp2[i] = array[i] + Math.max(dp2[i - 2], dp2[i - 3]);
            }
        }

        int result = Math.max(dp1[sticker.length - 1], dp1[sticker.length - 2]);
        result = Math.max(result, dp2[sticker.length - 1]);
        return Math.max(result, dp2[sticker.length - 2]);
    }

//    public int anotherSolution(int[] sticker) {
//        int size = sticker.length;
//
//        if (size <= 3) {
//            return Arrays.stream(sticker).max().getAsInt();
//        }
//
//        //각 인덱스까지의 스티커 최대 합을 저장할 배열
//        //첫 번째 스티커를 떼는 경우와 두 번째 스티커를 떼는 경우로 나눠서 저장
//        int[] dp1 = new int[size];
//        int[] dp2 = new int[size];
//
//        dp1[0] = dp1[1] = sticker[0];
//        dp2[0] = 0;
//        dp2[1] = sticker[1];
//
//        for (int i = 2; i < size - 1; i++) {
//            //이전에 구한게 더 크면 스티커 떼지 않고 유지
//            dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
//            dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
//        }
//
//        int i = size - 1;
//        dp1[i] = Math.max(dp1[i - 1], dp1[i - 2]);
//        dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
//
//        return Math.max(dp1[i], dp2[i]);
//    }

    public static void main(String[] args) {
        int[] sticker = {14, 6, 5, 11, 3, 9, 2, 10};
        Sticker stickerInstance = new Sticker();
        System.out.println(stickerInstance.solution(sticker));
        //System.out.println(stickerInstance.anotherSolution(sticker));
    }
}
