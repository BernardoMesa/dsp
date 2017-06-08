


def email_list():
#fhand.seek(0)
	fhand = open('faculty.csv')
	s = fhand.read()
	emails = re.findall('[a-zA-Z0-9.]+@\S*[a-zA-Z]', s)
	return emails

def write_csv():

	emails = email_list()

    fout = open('emails.csv', 'w')
    fout.write('list of emails\n')
    for email in emails:
        fout.write(email + '\n')
    fout.close()