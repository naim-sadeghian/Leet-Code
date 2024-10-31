class Solution:
    """
    Fibonacci using array

    Time Complexity: O(n) 
    Space Complexity: O(n) and 0(1) for the second version
    """
    def fib(self, n: int) -> int:
        fibo = [0,1]
        if (n >= 2):
            for i in range(2,n+1):
                fibo[0], fibo[1] = fibo[1], fibo[0] + fibo[1]
        return fibo[1]


    #Somehow Leetcode says that this version uses more memory and is slower... even though it doesnt create the whole array
    def fib2(self, n: int) -> int:
        fibo = [0,1]
        for i in range(2,n+1):
            fibo.append(fibo[-1]+fibo[-2])
        return fibo[n]