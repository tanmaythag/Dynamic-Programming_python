#N-th Tribonacci Number
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        s= 0
        f= 1
        se= 1
        
        if(n==0):
            return 0
        elif(n==1 or n==2):
            return 1
        for i in range(2,n):
            t_n = s+f+se
            s =f
            f = se
            se = t_n
        return t_n
        