# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.  Note:  Do not use Pandas library to complete this section.  

For Part 1, use of regular expressions is optional.  

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


#### Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> REPLACE THIS WITH YOUR RESPONSE

import re

fhand = fopen('faculty.csv')

d = dict()

for line in fhand:
	line = line.rstrip()
	flds = line.split(',')
	degree = flds[2]
	title = flds[3]
	d[degree] = d.get(degree,0)+1
	t[title] = t.get(title,0)+1	

emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]')
print(emails)



#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> REPLACE THIS WITH YOUR RESPONSE


#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> REPLACE THIS WITH YOUR RESPONSE
x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]')
print(x)


#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> REPLACE THIS WITH YOUR RESPONSE
dom = list[]
for i in x:
	pieces = i.split('@')
	if pieces[1] in dom: continue
	dom.append(pieces[1])



Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

fout = open('emails.csv','w')
for email in emails:
    fout.write(email + '\n')



### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

import re

fhand = fopen('faculty.csv')

d = dict()

for line in fhand:
	line = line.rstrip()
	flds = line.split(',')
	data = [flds[2],flds[3],flds[4]]
	#degree = flds[2]
	#title = flds[3]
	#email = flds[4]

	surname = r.findall('[a-zA-Z0-9]\S*$')
	if d.has_key(surname):
		d[surname] = d.get(surname,[]).append(data)
	#t[title] = t.get(title,0)+1



>> REPLACE THIS WITH YOUR RESPONSE

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> REPLACE THIS WITH YOUR RESPONSE

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

