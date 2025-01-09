class Solution:
    def reverse(self, x: int) -> int:
        num=0
        count=0
        y=abs(x)
        while y>=10:
            num+=y%10
            num*=10
            y=y//10
            count+=1
            print(count)
        num+=y%10
        if num >= ((2**31)-1) or num<=(-2**31):
            return 0
        if x<0:
            return-num
        return num