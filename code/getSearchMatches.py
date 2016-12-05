import csv


f2 = open('../data/searchmatches.csv', 'w')
with open('../data/results2.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for line in reader:
		f2.write(line['Id@github']+','+'https://www.linkedin.com/in/'+line['Link@linkedin']+'\n')