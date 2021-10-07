// 자바로 기존 문제 풀어보기 2일차
// 파이썬으로 풀 때는 콤비네이션 라이브러리가 쉽게 있어서 바로 가져다 썼지만
// 자바로 하기에는 변환해줘야할게 많아서 생각해보다가 
// '서로 다른 3개를 골라서 소수가 되는 경우'를 찾는게 정답이므로 힌트를 참조해서 코드를 작성했다
// 논리 자체는 너무 쉽지만 자바로 코테 구현하는게 익숙치 않아서 좀더 익숙해져야겠다.
// 2021.10.07

class Solution {

    public boolean isPrime(int number){
        if(number < 2){
            return false;
        }

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
        Solution sol = new Solution();
        System.out.println(sol.solution(array));
    }
}