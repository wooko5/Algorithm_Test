package carrot;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class P1 {
    private boolean[] visited;
    private List<String> list;

    public String[] solution(String[][] tickets) {
        String[] answer = {};
        list = new ArrayList<>();
        visited = new boolean[tickets.length];

        dfs("ICN", "ICN", tickets, 0);

        list.sort(Comparator.naturalOrder());

        answer = list.get(0).split(" ");

        return answer;
    }

    public void dfs(String start, String route, String[][] tickets, int count){
        if(count == tickets.length){
            list.add(route);
            return;
        }

        for(int i = 0; i < tickets.length; i++){
            if(!visited[i] && start.equals(tickets[i][0])){
                visited[i] = true;
                dfs(tickets[i][1], route + " " + tickets[i][1], tickets, count + 1);
                visited[i] = false;
            }
        }
    }
}
