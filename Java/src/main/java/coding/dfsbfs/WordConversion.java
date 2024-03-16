package coding.dfsbfs;

public class WordConversion {

    private int answer = 0;
    private boolean[] visited;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(begin, target, words, 0);
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
