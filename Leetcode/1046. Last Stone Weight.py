#implementing heap 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)
        while stones:
            s1 = -heappop(stones) 
            if not stones:  
                return s1
            s2 = -heappop(stones) 
            if s1 > s2:
                heappush(stones, s2-s1) 
        return 0 
    
# sort and insert
class Solution: 
	def lastStoneWeight(self, stones: List[int]) -> int: 
		stones.sort() 
		while stones: 
			s1 = stones.pop() # the heaviest stone 
			if not stones: # s1 is the remaining stone 
				return s1 
			s2 = stones.pop() # the second-heaviest stone; s2 <= s1 
			if s1 > s2: # we need to insert the remaining stone (s1-s2) into the list 
				# the remaining stone will be s1-s2
                # loop through stones to find the index to insert the stone
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= s1-s2:
                        stones.insert(i, s1-s2)
                        break
            # else s1 == s2; both stones are destroyed
		return 0 # if no more stones remain