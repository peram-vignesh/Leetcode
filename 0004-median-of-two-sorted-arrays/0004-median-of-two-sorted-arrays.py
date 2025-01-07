class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1=nums1+nums2
        list1.sort()
        if len(list1)%2==0:
            return (list1[len(list1)//2]+list1[len(list1)//2-1])/2
        else:
            return list1[len(list1)//2]
