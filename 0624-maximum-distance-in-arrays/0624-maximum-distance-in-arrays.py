class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minlist=[]
        maxlist=[]
        for i in arrays:
            minlist+=[i[0]]
            maxlist+=[i[-1]]
        if maxlist.index(max(maxlist))!=minlist.index(min(minlist)):
            return max(maxlist)-min(minlist)
        else:
            x=max(maxlist)
            y=min(minlist)
            maxlist.remove(x)
            minlist.remove(y)
            sums=[]
            sums+=[x-min(minlist)]
            sums+=[max(maxlist)-y]
            return max(sums)
        