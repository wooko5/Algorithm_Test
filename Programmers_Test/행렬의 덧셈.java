/*
파이썬으로 풀던 문제를 자바로도 똑같이 풀 수 있는 수준으로 만들기 위해 오늘부터 천천히 기초부터
자바로 코딩테스트를 풀기 위해 처음으로 푼 문제였다. 프로그래머스 레벨1의 문제로 매우 매우 쉽다
2021.10.06
*/

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];
        
        for(int i = 0; i < arr1.length; i++){
            for(int j = 0; j < arr1[0].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        
        return answer;
    }
}