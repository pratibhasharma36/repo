def fact(n):
	product=1
	for i in range(n):
		product=product*(i+1)
	return product
n=int(input())
print(fact(n))