import itertools

def f(N):
	L=list(N)
	ct=0
	for i in range(0,n-1):
		m=L[i]
		ind=i
		for j in range(i+1,n):
			if(L[j]<m):
				ind=j
				m=L[j]
		#print(j)
		for l in range(i,(i+ind+1)//2):
			(L[l],L[i+ind-l])=(L[i+ind-l],L[l])
		
		ct+=ind-i+1
	return ct

t=int(input())
for k in range(0,t):
	nc=input().split()
	n=int(nc[0])
	c=int(nc[1])
	M=[i+1 for i in range (n)]
	N=list(itertools.permutations(M))
	U=[]
	for e in N:
		U.append((e,f(e)))
	#print(U)
	j=0
	while(j<len(U)):
		if(U[j][1]==c):
			#print(j)
			A=U[j][0]
			break
		else:
			j+=1
	if(j==len(N)):
		print("Case "+"#"+str(k+1)+":"+" "+"IMPOSSIBLE")
	else:
		ans=""
		for K in range(0,n-1):
			ans+=str(A[K])+" "
		ans+=str(A[n-1])
		print("Case "+"#"+str(k+1)+":"+" "+ans)
