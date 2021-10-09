package com.programmers.java;

import java.util.Arrays;
// 프로그래머스 '행렬의 덧셈' 문제, 레벨 1, 2021.10.07, 1일차
public class AdditionOfMatrices {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];

        for(int i = 0; i < arr1.length; i++){
            for(int j = 0; j < arr1[0].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        AdditionOfMatrices additionOfMatrices = new AdditionOfMatrices();
        int[][] arr1 = {{1,2},{2,3}};
        int[][] arr2 = {{3,4},{5,6}};
        System.out.println(Arrays.deepToString(additionOfMatrices.solution(arr1, arr2)));
    }
}
