class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if (n > 9):
            return self.countNumbersWithUniqueDigits(9)
        elif (n == 0):
            return 1
        
        count = 1
        list2 = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(n):
            count = count * list2[i]
            
        if (n == 1):
            return count + 1
        else:
            return count + self.countNumbersWithUniqueDigits(n - 1)