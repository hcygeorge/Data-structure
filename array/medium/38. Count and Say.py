
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return '1'
        
        say = self.countAndSay(n-1)
        
        digits = []
        prev = None
        counter = None
        for d in say:
            if d != prev:
                if counter:
                    digits.append(counter)
                counter = [d, 1]
                prev = d
                
            else:
                counter[1] += 1
            
        digits.append(counter)
            
        count = ''
        
        for x in digits:
            count = count + str(x[1]) + str(x[0])
            
        return count