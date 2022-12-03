
import string
sum = 0

d = dict()
for letter in enumerate(string.ascii_lowercase, 1):
	d[letter[1]] = letter[0]
print(d)
with open('input.txt') as topo_file:
	for line in topo_file:

		mid = len(line.strip())//2
		com1 = line[:mid]
		com2 = line[mid:]
		priority = 0
		for i in com1:
			if i in com2:
				print(f'{i} in both')
				if i.isupper():
					tmp = i.lower();
					priority = d[tmp] + 26
				else:
					priority = d[i]	

		sum = sum + priority
print(sum)