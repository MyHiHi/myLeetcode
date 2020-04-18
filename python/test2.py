from collections import defaultdict
def canReorderDoubled(A) -> bool:
        A.sort();
        myMap=defaultdict(int);
        for a in A:
            myMap[a]+=1;
        cnt=0;
        
        for i in range(len(A)):
            print('**',A[i],myMap[A[i]],2*A[i],myMap[2*A[i]])
            
            if myMap[A[i]]>0 and myMap[2*A[i]]>0:
                myMap[A[i]]-=1;
                myMap[2*A[i]]-=1;
                cnt+=2
            print('map: ',myMap,'**',cnt)
        return cnt==len(A)
A=[1,2,1,-8,8,-4,4,-4,2,-2]
print(canReorderDoubled(A))