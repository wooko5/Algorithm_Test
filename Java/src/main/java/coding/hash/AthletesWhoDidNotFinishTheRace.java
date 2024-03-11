package coding.hash;

import java.util.HashMap;
import java.util.Map;

public class AthletesWhoDidNotFinishTheRace {

    public static void main(String[] args) {
        String[] participant = {"leo", "kiki", "eden"}; //{"mislav", "stanko", "mislav", "ana"}
        String[] completion = {"eden", "kiki"};

        System.out.println(solution(participant, completion));
    }

    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> participantMap = new HashMap<>();

        for (String name : participant) {
            if (participantMap.containsKey(name)) {
                int value = participantMap.get(name);
                value += 1;
                participantMap.put(name, value);
            } else {
                participantMap.put(name, 1);
            }
        }

        for (String name : completion) {
            if (participantMap.containsKey(name)) {
                int value = participantMap.get(name);
                value -= 1;
                participantMap.put(name, value);
            }
        }

        for (String name : participantMap.keySet()) {
            if (participantMap.get(name) > 0) {
                answer = name;
            }
        }

        return answer;
    }
}
