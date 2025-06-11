#2025-6-11 time: 15:21
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        if numRows == 0:
            return result
        
        first_row = [1]
        result.append(first_row)

        for i in range(1,numRows):
            prev = result[i-1]
            current = [1]

            for j in range(1,i):
                current.append(prev[j-1]+prev[j])

            current.append(1)
            result.append(current)

        return result


