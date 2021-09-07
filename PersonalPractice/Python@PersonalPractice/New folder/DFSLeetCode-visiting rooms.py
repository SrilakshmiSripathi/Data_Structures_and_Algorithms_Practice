class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] *len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            visiting = stack.pop()
            for key in rooms[visiting]:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)
        return all(seen)      
x = [[1],[2],[3],[]]
neww = Solution()
print (neww.canVisitAllRooms(x))
