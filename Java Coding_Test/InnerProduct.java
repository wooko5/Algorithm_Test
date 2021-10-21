package com.programmers.java;
// 프로그래머스 '내적' 문제, 레벨 1, 2021.10.07, 2일차
public class InnerProduct {
    public int solution(int[] a, int[] b) {
        int answer = 0;

        for(int i = 0; i < a.length; i++){
            answer += a[i] * b[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        InnerProduct innerProduct = new InnerProduct();
        int[] a = {1,2,3,4};
        int[] b = {-3,-1,0,2};
        System.out.println(innerProduct.solution(a, b));
    }
}
