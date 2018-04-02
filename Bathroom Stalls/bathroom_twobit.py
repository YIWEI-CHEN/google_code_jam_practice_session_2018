from collections import defaultdict

for t in range(int(input())):
	n, k = map(int, input().split())
	a = defaultdict(int)
	a[n] = 1
	while k > 0:
		m = max(a)
		n = min(a[m], k)
		k -= n
		a[m] -= n
		if a[m] == 0: del a[m]
		l = (m - 1) // 2
		r = m // 2
		a[l] += n
		a[r] += n

	print('Case #{}: {} {}'.format((t + 1), r, l))
