package coding.dfsbfs;

public class Network {

    private int answer = 0;

    public int solution(int n, int[][] computers) {

        if (n == 1) return 1;

        boolean[] visited = new boolean[n];

        for (int node = 0; node < n; node++) {
            if (!visited[node]) {
                dfs(node, n, computers, visited);
                answer += 1;
            }
        }

        return answer;
    }

    public void dfs(int node, int n, int[][] computers, boolean[] visited) {
        visited[node] = true;
//        System.out.println("node == " + node);
        for (int i = 0; i < n; i++) {
            if (!visited[i] && computers[node][i] == 1) {
                dfs(i, n, computers, visited);
            }
        }
    }
}
