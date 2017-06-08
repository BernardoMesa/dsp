import sys
import re

# Q1 how many degrees and their frequencies.
def degfreq():
	fhand = open('faculty.csv')

	headings = fhand.readline()

	d = dict()

	for line in fhand:
	    line = line.rstrip()
	    flds = line.split(',')
	    degrees = flds[1]
	    degrees = degrees.split()
	    for degree in degrees:
	        degree = degree.upper()
	        degree = degree.replace(".","")
	        d[degree] = d.get(degree,0)+1

	# print(headings)
	# print(d)
	return d


# Q2 how many titles and their frequencies.
def titfreq():
	fhand = open('faculty.csv')

	headings = fhand.readline()

	t = dict()

	for line in fhand:
	    line = line.rstrip()
	    flds = line.split(',')
	    title = flds[2]
	    title = title.split()
	    title = title[0]
	    title = title.lower()
	    #title = title.replace('is','of')
	    t[title] = t.get(title,0)+1

    #print(t)
    return t



# Q3 search for all email addresses and put them on a list.
# Print the list.

def emails():
#fhand.seek(0)
	fhand = open('faculty.csv')
	s = fhand.read()
	s = s.lower()
	email_list = re.findall('[a-zA-Z0-9.]+@\S*[a-zA-Z]', s)
	email_list.sort()

	return email_list

# Q4 Find how many different domains there are.
# Print the list of unique email domains.
def domains():

    #import re
    #fhand = open(emails)
    #s = fhand.read()
    s = " ".join(emails)
    s = s.lower()
    emails = re.findall('@(\S*[a-zA-Z])', s)
    emails = list(set(emails))
    emails.sort()
    return emails


#degfreq()