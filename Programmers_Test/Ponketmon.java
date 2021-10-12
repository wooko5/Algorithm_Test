package com.programmers.java;

import java.util.*;

/*
 * 처음에는 '조합(combination)'으로 풀어야하나 싶었지만 nums 배열의 최대 길이가 10000이기 때문에
 * 일반 컴퓨터로 계산하기 힘든 수준임을 알았고,
 * 결국 중복없는 자료구조인 'HashSet'을 이용해서 중복없는 숫자의 크기(hashSet.size())를 세고,
 * 그 숫자가 nums 배열을 2로 나눈 정수(half)보다 작다면 반환하고, 크다면 half를 반환하게 했다.
 * 매우 쉬운 문제 5분도 걸리지 않았다. 점점 파이썬보다 자바가 더 익숙해지는 기분이라 좋았다.
 * 프로그래머스 '폰켓몬' 문제, 레벨 1, 2021.10.12*/

public class Ponketmon {

    public int solution(int[] nums) {
        int half = nums.length / 2;

        HashSet<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            hashSet.add(num);
        }

        if (half > hashSet.size()) {
            return hashSet.size();
        } else {
            return half;
        }
    }

    public static void main(String[] args) {
        Ponketmon ponketmon = new Ponketmon();
        int[] nums = {3, 1, 2, 3};
        System.out.println(ponketmon.solution(nums));
    }
}
