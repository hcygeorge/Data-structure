class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = '0'

        idx_a, idx_b= len(a) - 1, len(b) - 1

        while idx_a >= 0 or idx_b >= 0 or carry == '1':
            ai = a[idx_a] if idx_a >= 0 else '0'
            bi = b[idx_b] if idx_b >= 0 else '0'

            if ai == bi:
                res.append(carry)
                carry = ai
            else:
                res.append(str(1- int(carry)))

            idx_a -= 1
            idx_b -= 1
        
        return ''.join(res[::-1])
