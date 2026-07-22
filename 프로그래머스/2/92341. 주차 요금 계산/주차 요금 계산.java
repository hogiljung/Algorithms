import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> totalParkingTimeByCar = calculateParkingTimes(records);
        
        return totalParkingTimeByCar.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .mapToInt(entry -> calculateFee(fees, entry.getValue()))
            .toArray();
    }
    
    private Map<String, Integer> calculateParkingTimes(String[] records) {
        Map<String, Integer> totalParkingTimeByCar = new HashMap<>();
        Map<String, Integer> entryTimeByCar = new HashMap<>();
        
        for (String record : records) {
            String[] parts = record.split(" ");
            
            int time = convertToMinutes(parts[0]);
            String carNumber = parts[1];
            String status = parts[2];
            
            if (status.equals("IN")) {
                entryTimeByCar.put(carNumber, time);
            } else {
                int entryTime = entryTimeByCar.remove(carNumber);
                int parkedMinutes = time - entryTime;
                
                totalParkingTimeByCar.merge(
                    carNumber,
                    parkedMinutes,
                    Integer::sum
                );
            }
        }
        
        int closingTime = 23 * 60 + 59;
        
        for (Map.Entry<String, Integer> entry : entryTimeByCar.entrySet()) {
            String carNumber = entry.getKey();
            int entryTime = entry.getValue();
            int parkedMinutes = closingTime - entryTime;
            
            totalParkingTimeByCar.merge(
                carNumber,
                parkedMinutes,
                Integer::sum
            );
        }
        
        return totalParkingTimeByCar;
    }
    
    private int convertToMinutes(String time) {
        String[] parts = time.split(":");
        
        int hour = Integer.parseInt(parts[0]);
        int minute = Integer.parseInt(parts[1]);
        
        return hour * 60 + minute;
    }
    
    private int calculateFee(int[] fees, int parkedMinutes) {
        if (parkedMinutes <= fees[0]) {
            return fees[1];
        }
        
        int extraTime = parkedMinutes - fees[0];
        int units = (extraTime + fees[2] - 1) / fees[2];
        
        return fees[1] + units * fees[3];
    }
}