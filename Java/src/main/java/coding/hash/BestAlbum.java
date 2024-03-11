package coding.hash;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class BestAlbum {
    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        System.out.println(solution(genres, plays));
    }

    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            if (map.containsKey(genres[i])) {
                int play = plays[i];
                play += map.get(genres[i]);
                map.put(genres[i], play);
            } else {
                map.put(genres[i], plays[i]);
            }
        }

        List<String> keyGenreList = new ArrayList<>(map.keySet());
        keyGenreList.sort((v1, v2) -> map.get(v2).compareTo(map.get(v1))); //value로 내림차순 완료

        List<Triple> triples = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            triples.add(new Triple(genres[i], plays[i], i));
        }


        triples.sort((v1, v2) -> v2.play - v1.play); //triples를 재생횟수를 기준으로 내림차순 정렬

        triples.forEach(v -> System.out.println("triple == " + v.genre + " " + v.play + " " + v.index));

        for (String genre : keyGenreList) {
            int count = 2;
            for (int j = 0; j < triples.size(); j++) {
                if (count > 0 && triples.get(j).genre.equals(genre)) {
                    answer.add(triples.get(j).index);
                    count -= 1;
                }
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    static class Triple {
        private String genre;
        private int play;
        private int index;

        public Triple(String genre, int play, int index) {
            this.genre = genre;
            this.play = play;
            this.index = index;
        }
    }

}
