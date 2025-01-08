class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        array1=[]
        while len(array1)<numRows:
            array1+=[[]]
        columns=0
        rows=0
        limit=numRows-1
        for i in s:
            if columns%limit==0 and rows<numRows:
                    array1[rows].append(i)
                    rows+=1
            elif columns%limit!=0:
                while rows<numRows:
                    array1[rows].append('')
                    rows+=1
                array1[rows-columns%limit-1][-1]=i
            if rows==numRows:
                columns+=1
                rows=0
        str1=''
        for i in array1:
            for x in i:
                str1+=x
        return str1
        


        