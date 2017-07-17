class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        array = [''] * numRows
        count = 0;
        dx = 1;
        for i in s:
            array[count] = array[count] + i
            dx = self.changeDX(count, numRows, dx)
            count = count + dx
            
        return ''.join(array)
    
    def changeDX(self, count, numRows, dx):
        temp = numRows - 1
        if count > 0 and count < temp:
            return dx
        elif count == 0 and dx == 1:
            return dx
        elif count == temp and dx == -1:
            return dx
        else: 
            return -dx