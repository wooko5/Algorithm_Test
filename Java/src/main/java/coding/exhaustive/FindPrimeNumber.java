package coding.exhaustive;

import java.util.*;

/**
 * level 2 소수찾기
 */
public class FindPrimeNumber {
    int[] array;
    int[] output;
    boolean[] visited;

    public static void main(String[] args) {
        String numbers = "011";
        System.out.println(new FindPrimeNumber().solution(numbers));
    }

    public int solution(String numbers) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();

        array = Arrays.stream(numbers.split("")).mapToInt(Integer::parseInt).toArray();
        output = new int[array.length];
        visited = new boolean[array.length];


        for (int i = 1; i <= array.length; i++) {
            permutation(array, output, visited, 0, i, list);
        }

        // List를 Set으로 변경
        Set<Integer> set = new HashSet<Integer>(list);

        // Set을 List로 변경
        List<Integer> newList =new ArrayList<Integer>(set);

        newList.forEach(System.out::println);

        for(int number : newList){
            if(isPrime(number)){
                answer += 1;
            }
        }

        return answer;
    }

    public void permutation(int[] arr, int[] output, boolean[] visited, int depth, int r, List<Integer> list) {

        if (depth == r) {
            StringBuilder stb = new StringBuilder();
            for (int i = 0; i < r; i++) {
                stb.append(Integer.toString(output[i]));
            }
            list.add(Integer.parseInt(stb.toString()));
            return;
        }

        for (int i = 0; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = arr[i];
                permutation(arr, output, visited, depth + 1, r, list);
                visited[i] = false;
            }
        }
    }

    public static boolean isPrime(int number) {
        if(number == 0 || number == 1){
            return false;
        }

        for(int i = 2; i <= Math.sqrt(number); i++){
            if(number % i == 0){
                return false;
            }
        }
        return true;
    }
}
