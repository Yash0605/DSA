"""
We can visualize this to be a graph problem.
Based on k value we can form a graph of digits where digits will be connected if they have a difference of k
While forming the number we can consider all the digites connected to each other
Eg: k=7 => In this case 1 and 8 will be connected, similarly 2 and 9, 7 and 0 etc will be connected.
As per graph sol we can traverse each nodes i.e digits 1-9 to get the final number => as these are valid 1st digits
Based on which digits are connected we can get the final number
"""


class Solution:
    def findCombinations(self, num, n, k, final_answer):
        # base case
        if n == 0:
            final_answer.append(num)
            return

        # consecutive numbers can be anywhere b/w 0 and 9
        last_digit = num % 10
        if last_digit + k < 10:
            self.findCombinations(num * 10 + last_digit + k, n - 1, k, final_answer)
        if k != 0 and last_digit - k >= 0:
            self.findCombinations(num * 10 + last_digit - k, n - 1, k, final_answer)

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        final_answer = []

        # The first digit in each valid number can start from 1-9
        for i in range(1, 10):
            self.findCombinations(i, n - 1, k, final_answer)

        return final_answer
