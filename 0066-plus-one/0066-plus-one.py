class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d1 = [str(i) for i in digits]
        d2 = list(str(int("".join(d1))+1))
        d3 = [int(n) for n in d2]
        return d3