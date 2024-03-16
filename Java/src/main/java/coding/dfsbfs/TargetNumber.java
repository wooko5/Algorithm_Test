package coding.dfsbfs;

/**
 * level 2 타겟넘버
 */
public class TargetNumber {

    private int answer;

    public int solution(int[] numbers, int target) {
        int index = 0;
        int sum = 0;

        dfs(numbers, target, index, sum);
        return answer;
    }
    public void dfs(int[] numbers, int target, int index, int sum) {

        if (index == numbers.length) {
            if (sum == target) {
                answer += 1;
            }
            return;
        }
        dfs(numbers, target, index + 1, sum + numbers[index]);
        dfs(numbers, target, index + 1, sum - numbers[index]);
    }
}
