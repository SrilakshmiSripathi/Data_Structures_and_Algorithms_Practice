from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        
        # create logs tuples for each user visite & sort them for timestamp
        sorted_logs = sorted(zip(timestamp, username, website))
        
        #sorted_logs = sorted(logs)
        #print("sorted_logs", sorted_logs)
        
        # store user website list map (would alreay be in order)
        userWebsiteMap = defaultdict(list)
        for log in sorted_logs:
            user = log[1]
            site = log[2]
            userWebsiteMap[user].append(site)
        print("userWebsiteMap", userWebsiteMap)
        # store the score of each pattern
        patternScoreMap = defaultdict(int)
        for websiteList in userWebsiteMap.values():
            combs = set(combinations(websiteList, 3))
            print("combs",combs)
            
            for comb in combs:
                patternScoreMap[comb] += 1
        print("patternScoreMap", patternScoreMap)
        # sort dictionary based on lexographical ordering
        sortedPatternScoreMap = sorted(patternScoreMap, key=lambda x:(-patternScoreMap[x], x))
        
        return sortedPatternScoreMap[0]

u = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
t = [1,2,3,4,5,6,7,8,9,10]
w = ["home","about","career","home","cart","maps","home","home","about","career"]



u1 = ["dowg","dowg","dowg"]
t1 = [158931262,562600350,148438945]
w1 = ["y","loedo","y"]


u2 = ["ua","ua","ua","ub","ub","ub"]
t2 = [1,2,3,4,5,6]
w2 = ["a","b","c","a","b","a"]

c = Solution()
print(c.mostVisitedPattern(u,t,w))
print(c.mostVisitedPattern(u1,t1,w1))
print(c.mostVisitedPattern(u2,t2,w2))


