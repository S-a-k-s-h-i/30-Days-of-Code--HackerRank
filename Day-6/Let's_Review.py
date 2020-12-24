t=int(input())

for i in range(0,t):
    evenlist=[]
    oddlist=[]
    S=input()
    for j in range(0,len(S)):
       if j%2==0:
         evenlist.append(S[j])
       else:
         oddlist.append(S[j])
    print(''.join(evenlist),''.join(oddlist))
