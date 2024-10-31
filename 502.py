class Solution:
    """
    Greedy: Sort by most profit and take the first you have enough capital for
            Do this k times

    Time Complexity: O(n^2)
    Space Complexity: O(1) and O(n) in second answer
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #my answer
        # profs = list(zip(capital, profits))
        # profs.sort(key=lambda x: x[1], reverse=True)
        # for _ in range(k):
        #     bestProfit = 0
        #     for i in range(len(profs)):
        #         if profs[i][0] <= w:
        #             bestProfit = profs[i][1]
        #             profs.pop(i)
        #             break

        #     if bestProfit == 0:
        #         break
        #     w += bestProfit

        # return w

        # Improvement by using heap
        profs = sorted( list(zip(capital, profits)) )
        i = 0
        heap = []
        for _ in range(k):
            bestProfit = 0
            while i < len(profs) and profs[i][0] <= w:
                heappush(heap, -profs[i][1])
                i += 1
            if not(heap):
                break
            w -= heappop(heap)

        return w