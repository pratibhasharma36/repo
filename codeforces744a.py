t=int(input())
for i in range(t):
	s=str(input())
	count=0
	ans=0
	m=0
	for i in range(len(s)):
		if s[i]=="A":
			count+=1
		elif s[i]=="B":
			ans+=1
		else:
			m+=1
	if ans>=count and ans>=m:
		if ans-count==m or ans-m==count:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
