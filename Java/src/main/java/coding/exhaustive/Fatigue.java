package coding.exhaustive;

/**
 * level 2 피로도
 * 순열과 DFS를 이용한 방법이 존재
 */
public class Fatigue {

    private int answer = 0;

    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        explore(k, dungeons, visited, 0);
        return answer;
    }

    public void explore(int k, int[][] dungeons, boolean[] visited, int depth) {

        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && k >= dungeons[i][0]) {
                visited[i] = true;
                explore(k - dungeons[i][1], dungeons, visited, depth + 1);
                visited[i] = false;

                System.out.println("i == " + i + " depth == " + depth + " dungeons[i][0] == " + dungeons[i][0] + " dungeons[i][1] == " + dungeons[i][1] + " k == " + k);
            }
        }

        if (depth > answer) {
            answer = depth;
        }
    }

    class Solution {
        private int[] index;
        private int answer = 0;

        public int solution(int k, int[][] dungeons) {

            index = new int[dungeons.length]; //[0, 0, 0]

            for (int i = 1; i < dungeons.length; i++) {
                index[i] = i; //[0, 1, 2]
            }

            permutation(index, 0, dungeons.length, dungeons.length, k, dungeons);

            return answer;
        }

        // 순열 구하기 : nCr (n개에서 r을 순열로 뽑아내기)
        // 사용 예시: permutation(arr, 0, n, r);
        void permutation(int[] arr, int depth, int n, int r, int k, int[][] dungeons) {

            if (depth == r) {
                int hp = k;
                int cnt = 0;
                for (int i = 0; i < r; i++) {
                    int j = arr[i];
                    if (hp >= dungeons[j][0]) {
                        hp -= dungeons[j][1];
                        if (hp > 0) {
                            cnt += 1;
                        }
                    }
                }
                answer = Math.max(cnt, answer);
                return;
            }

            for (int i = depth; i < n; i++) {
                swap(arr, depth, i);
                permutation(arr, depth + 1, n, r, k, dungeons);
                swap(arr, depth, i);
            }
        }

        void swap(int[] arr, int depth, int i) {
            int temp = arr[depth];
            arr[depth] = arr[i];
            arr[i] = temp;
        }
    }
}
