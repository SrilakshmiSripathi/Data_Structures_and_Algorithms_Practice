'''def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        strs = sorted(strs)
        print strs
        for st in strs:
            for i in st:
                if i not in dic:
                    dic[i] = dic.get(i,0) + 1
        return dic

inp = ["eat", "tea", "tan", "ate", "nat", "bat"]


print groupAnagrams(inp)
'''

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_ = {}
        res = []
        for i in range(len(strs)):
            mid = str(sorted(strs[i]))
            if mid in dict_.keys():
                dict_[mid].append(strs[i])
            else:
                dict_[mid] = []
                dict_[mid].append(strs[i])
        for item in dict_.keys():
            res.append(dict_[item])
        return res

inp = ["eat", "tea", "tan", "ate", "nat", "bat"]


print groupAnagrams(inp)
