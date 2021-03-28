# for i in range(0,n-1):
# 		m=L[i]
# 		ind=i
# 		for j in range(i+1,n):
# 			if(L[j]<m):
# 				ind=j
# 				m=L[j]
		
# 		for l in range(i,(i+ind+1)//2):
# 			(L[l],L[i+ind-l])=(L[i+ind-l],L[l])

def f(c,n):
	L=[0]*(n-1)
	L[0]=c-(n-1)
	k=n-1
	for i in range(0,n-1):
		if(L[i]>k):
			t=L[i]-k
			L[i+1]+=t
			L[i]=k
			k-=1
	return L

t=int(input())
for k in range(0,t):
	nc=input().split()
	n=int(nc[0])
	c=int(nc[1])
	M=[0]*n
	up=((n-1)*(n+2))//2
	if(c<(n-1) or c>up):
		flag=False
	else:
		flag=True
		L=[(n,i) for i in range (n)]
		indices=f(c,n)
		#print(indices)
		for i in range(0,n-1):
			L[i+indices[i]]=(i+1,L[i+indices[i]][1])
			ind=i+indices[i]
			for l in range(i,(i+ind+1)//2):
				(L[l],L[i+ind-l])=(L[i+ind-l],L[l])

		N=[0]*n
		for i in range(0,n):
			N[L[i][1]]=L[i][0]
			
				
	if(flag==False):
		print("Case "+"#"+str(k+1)+":"+" "+"IMPOSSIBLE")
	else:
		ans=""
		for K in range(0,n-1):
			ans+=str(N[K])+" "
		ans+=str(N[n-1])
		print("Case "+"#"+str(k+1)+":"+" "+ans)