class Solution:
    def romanToInt( s: str) -> int:
		#A dictionary to store the roman values
        symbols={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        l=[]
		#If only one symbol is given, below condition can directly return the value
        if s in symbols:
            return symbols[s]
        for i in s:
            l.append(i)
        i=0
        while i<len(s):
            if i<len(l)-1:
                if symbols[l[i]]>=symbols[l[i+1]]:
                    sum=sum+symbols[l[i]]
                    i+=1
                else:
                    sum=sum+(symbols[l[i+1]]-symbols[l[i]])
                    i+=2
            #if the last index roman value is greater than its previous one, the condition is             #satisfied in the above else
			#If the last roman value is smaller, then the above 2 conditions does not satisy               #that.
			#the value is ignored, so i added other elif to add that last value
            elif i==len(s)-1:
                if symbols[l[i]]<=symbols[l[i-1]]:
                    sum+=symbols[l[i]]
                    i+=1

        return sum

test=Solution.romanToInt("XV")

print(test)
