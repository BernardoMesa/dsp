# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    
    f_handle = open(filename,'r')

    string_list = []

    for line in f_handle:
        #print(line)
        line_contents = line.split(',')
        string_list.append(line_contents)
        
    return string_list
        


def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    diff = None
    idx = None
    #max = len(goals)
    for i in range(0,len(goals)):
        line = goals[i]
        try:
            gf = int(line[5])
            ga = int(line[6])
            if diff == None or abs(ga-gf)<diff:
                #team = line[0]
                diff = abs(ga-gf)
                idx = i
        except:
            pass
    
    return idx
    
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    line = parsed_data[index_value]
    return line[0]


footballTable = read_data('football.csv')
#print(footballTable)
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow,footballTable)))

# fname = 'football.csv'

# f_handle = open(fname,'r')

# diff = None

# for line in f_handle:

# 	print(line)
# 	contents = line.rstrip("\n")
# 	contents = line.strip()
# 	contents = line.split(',')

# 	try:
# 		gf = int(contents[5])
# 		ga = int(contents[6])
# 		print(abs(ga-gf))
# 		if diff == None or abs(ga-gf)<diff:
# 			team = contents[0]
# 			diff = abs(ga-gf)
# 	except:
# 		pass



# print('The team with smallest difference is: ',team)




