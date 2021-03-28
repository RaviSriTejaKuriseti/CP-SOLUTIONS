t=int(input())
for k in range(0,t):
	xys=input().split()
	x=int(xys[0])
	y=int(xys[1])
	s=xys[2]
	n=len(s)
	i=0
	j=0
	cost=0
	while(i<n):
		if(s[i]=="?"):
			j=i
			while(j<n and s[j]=="?"):
				j+=1
			if(j==n or i==0):
				cost+=0
			else:
				if(s[i-1]!=s[j]):
					if(s[i-1]=="J"):
						cost+=y
					else:
						cost+=x
				else:
					cost+=0
			i=j
		else:
			i+=1

	for u in range(0,n-1):
		if(s[u]=="C" and s[u+1]=="J"):
			cost+=x
		elif(s[u]=="J" and s[u+1]=="C"):
			cost+=y
		else:
			cost+=0



		
		
	print("Case "+"#"+str(k+1)+":"+" "+str(cost))