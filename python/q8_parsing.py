# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

fname = 'football.csv'

f_handle = open(fname,'r')

diff = None

for line in f_handle:

	print(line)
	contents = line.rstrip("\n")
	contents = line.strip()
	contents = line.split(',')

	try:
		gf = int(contents[5])
		ga = int(contents[6])
		print(abs(ga-gf))
		if diff == None or abs(ga-gf)<diff:
			team = contents[0]
			diff = abs(ga-gf)
	except:
		pass



print('The team with smallest difference is: ',team)

