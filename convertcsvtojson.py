import json
import io
import csv
import codecs


f1 = open('github-users.csv', 'rb')
reader = csv.DictReader(f1)

f2 = open('cleaned_data.json', 'w')
for user in reader:
	print user
	f2.write((json.dumps(user, ensure_ascii=False)+'\n'))

f2.close()