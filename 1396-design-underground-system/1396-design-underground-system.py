class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.travel_times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
                
        end_station = stationName
        
        time_diff = t - start_time
        
        key = (start_station, end_station)
        
        if key not in self.travel_times:
            self.travel_times[key] = []
        self.travel_times[key].append(time_diff)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        
        # sum // len
        
        travel_times = self.travel_times[key]
        
        return sum(travel_times) / len(travel_times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)