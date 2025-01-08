class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        list1=[]
        count=0
        for i in words:
            for x in words:
                if i in x:
                    count+=1
                if count==2:
                    list1+=[i]
                    break
            count=0
        return list1