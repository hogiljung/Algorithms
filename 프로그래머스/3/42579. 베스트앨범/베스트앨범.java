import java.util.*;

/*
장르별 재생횟수로 오름차순
각 장르에서 재생횟수 내림차순, 고유번호 오름차순으로
*/

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genrePlayMap = new HashMap<>();
        Map<String, List<Song>> songGenreMap = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            genrePlayMap.put(genres[i], genrePlayMap.getOrDefault(genres[i], 0) + plays[i]);
            
            List<Song> songs = songGenreMap.getOrDefault(genres[i], new ArrayList<>());
            songs.add(new Song(i, plays[i]));
            songGenreMap.put(genres[i], songs);
        }
        
        List<String> genreList = genrePlayMap.entrySet()
            .stream()
            .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
            .map(Map.Entry::getKey)
            .toList();
        
        List<Integer> answer = new ArrayList<>();
        
        for (String g : genreList) {
            List<Song> songs = songGenreMap.get(g)
                .stream()
                .sorted((a, b) -> {
                    int compare = Long.compare(b.plays, a.plays); 
                    if (compare == 0) {
                        return Integer.compare(a.id, b.id);
                    }
                    return compare;
                })
                .limit(2)
                .toList();
            
            for (Song s : songs) {
                answer.add(s.id);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    class Song {
        int id;
        long plays;
        
        Song(int id, long plays) {
            this.id = id;
            this.plays = plays;
        }
    }
}