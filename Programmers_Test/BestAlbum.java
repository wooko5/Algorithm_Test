package programmers;

import java.util.*;

class Songs {

    private String genre;
    private int play;
    private int index;

    public Songs(int index, String genre, int play) {
        this.index = index;
        this.genre = genre;
        this.play = play;
    }

    public String getGenre() {
        return genre;
    }

    public int getPlay() {
        return play;
    }

    public int getIndex() {
        return index;
    }
}

public class BestAlbum {

    public static int[] solution(String[] genres, int[] plays) {

        Map<String, Integer> song = new HashMap<>(); // 장르선택을 위한 해시맵
        List<Songs> songInfo = new ArrayList<>();
        List<Integer> index = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            if (!song.containsKey(genres[i]))
                song.put(genres[i], plays[i]);
            else
                song.put(genres[i], song.get(genres[i]) + plays[i]);

            songInfo.add(new Songs(i, genres[i], plays[i]));
        }

        // 장르 인기순 정렬
        List<String> popularity = new ArrayList<>(sortByValue(song));

        for (String genre : popularity) {
            List<Songs> bestAlbum = new ArrayList<>();

            for (int i = 0; i < songInfo.size(); i++) {
                if (songInfo.get(i).getGenre().equals(genre))
                    bestAlbum.add(songInfo.get(i));
            }

            bestAlbum.sort(new Comparator<Songs>() {
                @Override
                public int compare(Songs o1, Songs o2) {
                    if (o1.getPlay() > o2.getPlay()) {
                        return -1;
                    } else if (o1.getPlay() == o2.getPlay()) {
                        return 0;
                    } else {
                        return 1;
                    }
                }
            });

            for(int i = 0 ; i<bestAlbum.size(); i++) {
                if(i < 2) {
                    index.add(bestAlbum.get(i).getIndex());
                }
            }

        }

        int[] answer = new int[index.size()];
        for(int i = 0; i<index.size(); i++) {
            answer[i] = index.get(i);
        }

        return answer;
    }

    public static List<String> sortByValue(Map<String, Integer> map) {
        List<String> key = new ArrayList<>(map.keySet());

        key.sort(new Comparator<Object>() {
            @Override
            public int compare(Object o1, Object o2) {
                Object ob1 = map.get(o1);
                Object ob2 = map.get(o2);

                return ((Comparable<Object>) ob2).compareTo(ob1);
            }
        });

        return key;
    }
}