package coding.stackAndQueue;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * level 2 다리를 지나는 트럭
 */
public class TruckPassingOverTheBridge {
    public static void main(String[] args) {
        int bridge_length = 2; //큐의 최대 크기
        int weight = 10; //큐의 담을 수 있는 최대 합계
        int[] truck_weights = {7, 4, 5, 6}; //순서대로 트럭의 무게
        System.out.println(solution(bridge_length, weight, truck_weights));
    }

    private static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int time = 1;

        Queue<Integer> bridge = new LinkedList<>(); //다리 bridge 정수 큐 만들기
        Queue<Integer> truck = new LinkedList<>(); //대기 중인 truck 정수 큐 만들기


        for (int tr : truck_weights) {
            truck.add(tr);
        }

        bridge.add(truck.poll()); //대기 중인 첫번째 트럭을 다리에 올려놓기

        while (!bridge.isEmpty() && !truck.isEmpty()) {
            time += 1;

            if (bridge.size() < bridge_length) {
                int sum = Arrays.stream((bridge.stream().mapToInt(i -> i).toArray())).sum(); //다리에 올라간 트럭의 총 무게
                if (sum + truck.peek() <= weight) {
                    bridge.add(truck.poll());
                }else {
                    bridge.add(0);
                }
            } else {
                bridge.poll(); //다리에 트럭이 모두 올라갔으니 나가자
            }

            System.out.println("time == " + time + " bridge == " + Arrays.toString(bridge.toArray()) + " truck == " + Arrays.toString(truck.toArray()));
        }

        return time;
    }
}
