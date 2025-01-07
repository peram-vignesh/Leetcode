class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numcopy=nums.copy()
        numcopy.sort()
        max=-1
        min=0
        while True:
            sums=numcopy[max]+numcopy[min]
            if sums>target:
                max-=1
            elif sums<target:
                min+=1
            elif sums==target:
                x=nums.index(numcopy[min])
                y=nums.index(numcopy[max])
                if x==y:
                    nums.remove(nums[x])
                    y=nums.index(numcopy[max])+1
                return[x,y]
        