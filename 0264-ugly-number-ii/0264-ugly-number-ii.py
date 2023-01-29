class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        ugly_numbers = [1]
        
        i2, i3, i5 = 0, 0, 0
        
        while len(ugly_numbers) < n:
            next_multiple_of_2 = ugly_numbers[i2] * 2
            next_multiple_of_3 = ugly_numbers[i3] * 3
            next_multiple_of_5 = ugly_numbers[i5] * 5
            
            next_ugly_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            
            if next_ugly_number == next_multiple_of_2:
                i2 += 1
                
            if next_ugly_number == next_multiple_of_3:
                i3 += 1
                
            if next_ugly_number == next_multiple_of_5:
                i5 += 1
                
            ugly_numbers.append(next_ugly_number)
        return ugly_numbers[-1]
        