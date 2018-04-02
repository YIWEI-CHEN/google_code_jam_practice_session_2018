for i in range(1,int(input())+1):
	m = -1
	d,j = map(float,input().split())
	for k in range(int(j)):
		x,s = map(float,input().split())
		m = max(m,(d-x)/s)
	d = d/m
	print('Case #%d: %f'%(i,d))