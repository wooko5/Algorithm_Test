package coding.dfsbfs;

import java.util.LinkedList;
import java.util.Queue;

public class WordConversion {

    private int answer = 0;
    private boolean[] visited;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
//        dfs(begin, target, words, 0);
        bfs(begin, target, words);
        return answer;
    }

    public void dfs(String begin, String target, String[] words, int count) {
        if (begin.equals(target)) {
            answer = count;
            return;
        }

        for (int i = 0; i < words.length; i++) {
            if (!visited[i] && check(begin, words[i])) {
                visited[i] = true;
                dfs(words[i], target, words, count + 1);
                visited[i] = false;
            }
        }
    }

    public void bfs(String begin, String target, String[] words) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(begin, 0));

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            String word = node.word;
            int index = node.index;
            visited[index] = true;
            if (word.equals(target)) {
                break;
            }

            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && check(word, words[i])) {
                    answer += 1;
                    queue.add(new Node(words[i], i));
                }
            }
        }
    }

    private static class Node {
        private String word;
        private int index;

        public Node(String word, int index) {
            this.word = word;
            this.index = index;
        }
    }

    public boolean check(String original, String word) {
        int count = 0;

        //두 단어의 차이가 알파벳 1개인 경우만 색출하는 메서드
        for (int i = 0; i < original.length(); i++) {
            if (original.charAt(i) != word.charAt(i)) {
                count += 1;
            }
        }

        return count == 1;
    }
}
