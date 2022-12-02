max_cals = 0
sec_max_cals = 0
thr_max_cals = 0

cur_cals = 0
with open('input.txt') as topo_file:
	for line in topo_file:

		if line.strip() == "":
		
			if cur_cals > max_cals:
				thr_max_cals = sec_max_cals
				sec_max_cals = max_cals
				max_cals = cur_cals
			elif cur_cals > sec_max_cals:
				thr_max_cals = sec_max_cals
				sec_max_cals = cur_cals
			elif cur_cals > thr_max_cals:
				thr_max_cals = cur_cals

			cur_cals = 0
			continue

		cur_cals = cur_cals + int(line.strip())


print(max_cals)
print(sec_max_cals)
print(thr_max_cals)
print(max_cals + sec_max_cals + thr_max_cals)