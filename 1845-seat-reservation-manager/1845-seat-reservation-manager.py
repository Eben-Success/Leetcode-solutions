class SeatManager:

    def __init__(self, n: int):
        self.seat_list = list(range(1, n + 1))
        heapify(self.seat_list)
        

    def reserve(self) -> int:
        return heappop(self.seat_list)
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seat_list, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)