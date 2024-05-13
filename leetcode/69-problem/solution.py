class Solution(object):
    def reve(self, n):
        b = n
        rev = 0
        while(b>0):
            dig = b%10
            rev = rev*10 + dig
            b = b//10
        
        return rev
    def maximum69Number (self, n):
        ch = 0
        rev = 0
        r = self.reve(n)
        while(r>0):
            dig = r%10
            if dig == 6 and ch == 0:
                dig = 9
                ch = 1
            rev = rev*10 + dig
            r = r//10
            
        return rev
        
