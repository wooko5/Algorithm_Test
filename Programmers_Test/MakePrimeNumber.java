package com.programmers.java;
// 프로그래머스 '소수 만들기' 문제, 레벨 1, 2021.10.07, 2일차
class MakePrimeNumber {

    public boolean isPrime(int number){
        if(number < 2){
            return false;
        }
        // int()가 아닌 (int)로 캐스팅해야함으로 주의하자!! 이걸로 겁나 틀림
        for(int i = 2; i <= (int)Math.sqrt(number); i ++){
            if(number % i == 0){
                return false;
            }
        }
        return true;
    }


    public int solution(int[] nums) {
        int answer = 0;

        for(int i = 0; i < nums.length - 2; i ++){
            for(int j = i + 1; j < nums.length - 1; j ++){
                for(int k = j + 1; k < nums.length; k ++ ){
                    if(isPrime(nums[i] + nums[j] + nums[k])){
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] array = {1,2,3,4};
        MakePrimeNumber sol = new MakePrimeNumber();
        System.out.println(sol.solution(array));
    }
}
