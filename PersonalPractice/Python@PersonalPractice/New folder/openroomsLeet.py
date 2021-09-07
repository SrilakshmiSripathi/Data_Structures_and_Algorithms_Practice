class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        for num, key in enumerate(rooms):
            if room[num] == 
        while len(rooms) != 0:
            for num, key in enumerate(rooms):
                print num,key
                for k in key:
                    print k
                    if k in rooms[num]:
                        rooms.remove(rooms[num])
                        print rooms
        if rooms == []:
            return True
        else:
            return False
                
            
                
            
        
        
x = [[1],[2],[3],[]]
neww = Solution()
print neww.canVisitAllRooms(x)
