for i in xrange(1,input()+1):
	m = -1
	d,j = map(float,raw_input().split())
	for k in xrange(int(j)):
		x,s = map(float,raw_input().split())
		m = max(m,(d-x)/s)
	d = d/m
	print 'Case #%d: %f'%(i,d)