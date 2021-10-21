package programmers;

import java.util.*;
/*
큐를 이용한 문제라고 하지만 ArrayList, Set을 이용해서 풀었고, 결국 정렬된 ArrayList가 큐의 역할을 한 것 같다
* 프로그래머스 '기능개발' 문제, 레벨 2, 2021.10.19*/
class FunctionDevelopment {
    public int[] solution(int[] progresses, int[] speeds) {
        double temp;
        int result;
        List<Integer> array = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            temp = 100 - progresses[i];

            if (temp / speeds[i] != (int) (temp / speeds[i])) {
                result = (int) (temp / speeds[i]) + 1;
            } else {
                result = (int) (temp / speeds[i]);
            }

            array.add(result);
        }

        for (int i = 0; i < array.size() - 1; i++) {
            int first = array.get(i);
            int second = array.get(i + 1);
            if(second < first){
                array.set(i+1, first);
            }
        }

        Set<Integer> sourceSet = new HashSet<>(array);
        int[] answer = new int[sourceSet.size()];
        List<Integer> targetList = new ArrayList<>(sourceSet);
        targetList.sort(Comparator.naturalOrder());

        for(int i = 0; i < targetList.size(); i++){
            int count = 0;
            for(int j = 0; j < array.size(); j++){
                if(targetList.get(i) == array.get(j)){
                    count += 1;
                }
            }
            answer[i] = count;
        }

        return answer;
    }
}
