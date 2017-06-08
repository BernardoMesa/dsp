import sys
import os
import re

# Q6. Create a dictionary in the below format:
#faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
def py_dict():

    fhand = open('faculty.csv')

    headings = fhand.readline()

    d = dict()

    for line in fhand:
        line = line.strip()
        flds = line.split(',')
        # for i in range(0,len(flds)):
        # 	temp_str = flds[i]
        # 	temp_str = temp_str.strip()
        # 	flds[i] = temp_str

        #last_name = re.findall('\S*$',flds[0])
        last_name = flds[0].split()[-1].strip()
        #last_name = last_name[0].strip()
        #print(last_name + "\n")

        #title = re.findall('^.*Professor',flds[2])
        #title = title[0].strip()
        title = flds[2].strip()
        degrees = flds[1]#.strip()
        email = flds[3].strip()
        sublist = [degrees,title,email]
        #degrees = degrees.split()
        #for degree in degrees:
        #	d[degree] = d.get(degree,0)+1
        if last_name in d:
            val = d[last_name]
            val.append(sublist)
            d[last_name] = val
        else:
            d[last_name] = [sublist]

    return d

# Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }


def py_dict2():

# Complete the function below.

def get_dict():
    fhand = open('faculty.csv')
    
    headings = fhand.readline()
    
    d = dict()
    
    for line in fhand:
        line = line.strip()
        flds = line.split(',')
        
        #name = flds[0].split()
        #name = (name[0],name[-1])
        name = tuple(flds[0].split())
        
        title = flds[2].strip()
        degrees = flds[1]#.strip()
        email = flds[3].strip()
        sublist = [degrees,title,email]
        d[name]=sublist
        
    return d
        

	for key in d:
		print(key)
		print(d[key])
	print('\n')
	print(len(d))

	print('\n')

	print(d)
