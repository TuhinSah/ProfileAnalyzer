import json
import codecs
import unicodecsv as csv


with open('data/ProfileCardData 2.json', 'r') as f1:
	d = json.loads(f1.read())

with open('data/linkedinsearch2.csv', 'wb') as f1:
	f2 = csv.writer(f1, encoding='utf-8')
	f2.writerow(['Name', 'Job','Industry','Country','Link'])
	#f1.write('Name,Job,Industry,Country,Link\n')
	for u in d:
		f2.writerow([u['name'],u['job'],u['industry'],u['country'],u['link']])
		#f1.write(u['name']+','+u['job']+','+u['industry']+','+u['country']+','+u['link']+'\n')
