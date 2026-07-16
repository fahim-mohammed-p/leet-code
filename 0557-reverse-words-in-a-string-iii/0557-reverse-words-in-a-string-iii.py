class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        rev_words=[]
        for word in words:
            rev_words.append(word[::-1])

        new=' '.join(rev_words)
        
        return new
        