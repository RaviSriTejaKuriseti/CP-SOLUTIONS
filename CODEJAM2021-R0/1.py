t=int(input())
for k in range(0,t):
	n=int(input())
	L=list(map(int,input().split()))
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

		
		
	print("Case "+"#"+str(k+1)+":"+" "+str(ct))