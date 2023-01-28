### Brute Force
​
```
class SeatManager:
def __init__(self, n):
self.seat_list = list(range(1, n+1)
def reserve(self):
minimum = min(self.seat_list)
self.seat_list.remove(minimum)
return minimum
def unreserve(self, seatNumber):
self.seat_list.append(seatNumber)
```