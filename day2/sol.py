score = 0

WIN = 6
LOSS = 0
TIE = 3

ROCK = 1
PAPER = 2
SCISSORS = 3

with open('input.txt') as topo_file:
	for line in topo_file:
		x = line.split()
		#A = rock, B = paper C = scissors
		#X = rock, Y = paper Z = scissors
		round = 0
		match x:
			case ['A', 'X']:
				print("I tie")
				round =  ROCK + TIE
			case ['A', "Y"]:
				print("I lose")
				round =  PAPER + WIN
			case ['A', 'Z']:
				print("I win")
				round =  SCISSORS + LOSS
			case ['B', 'X']:
				print("I Win")
				round =  ROCK + LOSS
			case ['B', 'Y']:
				print("I tie")
				round =  PAPER + TIE
			case ['B', 'Z']:
				print("I lose")
				round = SCISSORS + WIN
			case ['C', 'X']:
				print("I lose")
				round =  ROCK + WIN
			case ['C', 'Y']:
				print("I win")
				round =  PAPER + LOSS
			case ['C', 'Z']:
				print("I tie")
				round =  SCISSORS + TIE
		score = score + round

print(score)