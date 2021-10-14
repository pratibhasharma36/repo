t=int(input())
for i in range(t):
	a,b,c=list(map(int,input().split()))
	x=max(a,b,c)
	if a==b==c:
		print(1,end=" ")
		print(1,end=" ")
		print(1)
	elif x==a==b or x==b==c or x==c==a:

		if x==c==b:
			print(x-a+1,end=" ")
			print(1,end=" ")
			print(1)
		elif x==c==a:
			print(1,end=" ")
			print(x-b+1,end=" ")
			print(1)
		elif x==a==b:
			print(1,end=" ")
			print(1,end=" ")
			print(x-c+1)
	else:
		if x==a:
					print(0,end=" ")
					print(x-b+1,end=" ")
					print(x-c+1)
		elif x==b:
					print(x-a+1,end=" ")
					print(0,end=" ")
					print(x-c+1)
		elif x==c:
					print(x-a+1,end=" ")
					print(x-b+1,end=" ")
					print(0)


