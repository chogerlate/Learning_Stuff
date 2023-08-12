class Solution:
    def mySqrt(self, x: int) -> int:
        """
        the Babylonian method, also known as Heron's method. It is an iterative algorithm that refines the estimate until it converges to the actual square root. Here's how you can 
        """
        # normal case
        if x==0 :
            return 0

        # initial guess
        xn = x/2

        while True:
            # new_guess = average of the 2 value xn and a/xn
            new_xn = 0.5 * (xn+ x/xn)
            print("estimate: ",new_xn)
            if abs(xn - new_xn) < 1e-10:
                break
            xn = new_xn
        return int(xn)
