# tips: 利用hashmap和sorted

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in group:
                group[sorted_word].append(word)
            else:
                group[sorted_word] = [word]
        
        return [x for x in group.values()]