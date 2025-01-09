class Solution:
    def myAtoi(self, s: str) -> int:
        x=0
        count=0
        num=0
        for i in s:
            if i not in '+-0123456789 ':
                return x*((-1)**count)
            elif i not in '0123456789' and num==1:
                return x*((-1)**count)
            elif i==' ':
                continue
            else:
                num=1
                if i in '0123456789':
                    x*=10
                    x+=int(i) 
                    print(x)
                    if x>=2**31:
                        print(count)
                        x=(2**31)+(count-1)
                elif i=='-':
                    count+=1
        return x*((-1)**count)