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
		#X = lose, Y = tie Z = win
		round = 0
		match x:
			case ['A', 'X']:
				round =  SCISSORS + LOSS
			case ['A', "Y"]:
				round =  ROCK + TIE
			case ['A', 'Z']:
				round =  PAPER + WIN
			case ['B', 'X']:
				round =  ROCK + LOSS
			case ['B', 'Y']:
				round =  PAPER + TIE
			case ['B', 'Z']:
				round = SCISSORS + WIN
			case ['C', 'X']:
				round =  PAPER + LOSS
			case ['C', 'Y']:
				round =  SCISSORS + TIE
			case ['C', 'Z']:
				round =  ROCK + WIN
		score = score + round

print(score)