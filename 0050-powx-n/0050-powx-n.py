class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        """
        Edge cases
        if n is 0: x^ 0 == 1

        if n is even
        x^n/2 * x^n/2
        
        if n is odd
        x * pow(x, n - 1)

        if n < 0:
            E.g: 3^-2 = (1/3)^2
        """

        # check if n  == 0
        if n == 0:
            return 1
        
        # check if n < 0
        
        elif n < 0:
            return self.myPow(1/x, -n)
        
        # if n is even

        elif n % 2 == 0:
            temp = self.myPow(x, n/2)
            return temp * temp
            # return self.myPow(x, n/2) * self.myPow(x, n/2)

        else:
            return x * self.myPow(x, n - 1)
        
       