import json
import codecs
import unicodecsv as csv


with open('data/ProfileCardData 2.json', 'r') as f1:
	d = json.loads(f1.read())

with open('data/linkedinsearch3.csv', 'wb') as f1:
	f2 = csv.writer(f1, encoding='utf-8')
	f2.writerow(['Name', 'Current','Industry','Country','Link','Education', 'Previous'])
	#f1.write('Name,Job,Industry,Country,Link\n')
	for u in d:
		f2.writerow([u['name'],u['current'],u['industry'],u['country'],u['link'].split('/')[-1],
			','.join(u['education']), ','.join(u['previous'])])
		#f1.write(u['name']+','+u['job']+','+u['industry']+','+u['country']+','+u['link']+'\n')
