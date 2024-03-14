package coding.stackAndQueue;

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
        int time = 0;
        int sum = 0;
        Queue<Integer> bridge = new LinkedList<>(); //다리 bridge 정수 큐 만들기

        for (int truck : truck_weights) {

            while (true) {

                if (bridge.isEmpty()) { //다리에 트럭이 없는 경우
                    sum += truck;
                    bridge.add(truck);
                    time += 1;
                    break;
                } else if (bridge.size() == bridge_length) { //다리에 트럭이 가득 찬 경우
                    sum -= bridge.poll();
                } else { //다리에 차량이 있는데 가득 차지 않은 경우
                    if (sum + truck <= weight) { //다리의 올라간 차량 무게 + 다가올 차량 무게 <= 최대 다리지원
                        sum += truck;
                        bridge.add(truck);
                        time += 1;
                        break;
                    } else {
                        bridge.add(0);
                        time += 1;
                    }
                }
            }

//            System.out.println("time == " + time + " bridge == " + Arrays.toString(bridge.toArray()) + " truck == " + truck);
        }

        return time + bridge_length; //마지막 트럭이 다리를 빠져나오는 시간(bridge_length)을 더해줘야 모든 트럭이 다리룰 건넘
    }
}
