from collections import defaultdict
def canReorderDoubled(A) -> bool:
        # A.sort();
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

** 1 2 2 2
map:  defaultdict(<class 'int'>, {1: 1, 2: 1, -8: 1, 8: 1, -4: 2, 4: 1, -2: 1}) ** 2
** 2 1 4 1
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 1, 8: 1, -4: 2, 4: 0, -2: 1}) ** 4
** 1 1 2 0
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 1, 8: 1, -4: 2, 4: 0, -2: 1}) ** 4
** -8 1 -16 0
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 1, 8: 1, -4: 2, 4: 0, -2: 1, -16: 0}) ** 4
** 8 1 16 0
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 1, 8: 1, -4: 2, 4: 0, -2: 1, -16: 0, 16: 0}) ** 4
** -4 2 -8 1
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 0, 8: 1, -4: 1, 4: 0, -2: 1, -16: 0, 16: 0}) ** 6
** 4 0 8 1
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 0, 8: 1, -4: 1, 4: 0, -2: 1, -16: 0, 16: 0}) ** 6
** -4 1 -8 0
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 0, 8: 1, -4: 1, 4: 0, -2: 1, -16: 0, 16: 0}) ** 6
** 2 0 4 0
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 0, 8: 1, -4: 1, 4: 0, -2: 1, -16: 0, 16: 0}) ** 6
** -2 1 -4 1
map:  defaultdict(<class 'int'>, {1: 1, 2: 0, -8: 0, 8: 1, -4: 0, 4: 0, -2: 0, -16: 0, 16: 0}) ** 8