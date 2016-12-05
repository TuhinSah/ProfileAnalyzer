import cPickle as pickle 
import glob
import codecs
import unicodecsv as csv

def xstr(s):
	if s is None:
		return ''
	return s


files = glob.glob('data/searchpages/*.html')
needed = []
for file in files:
	needed.append(file.split('/')[2][:-5])


users = pickle.load(open('allusersinfo.p', 'rb'))

with open('data/searchusers.csv', 'wb') as f1:
	f2 = csv.writer(f1, encoding='utf-8')
	f2.writerow(['Id','Name', 'Company','Email','Bio','Blog','Location'])
	#f1.write('Name,Compan,Email,Bio,Blog,Location\n')
	for user in needed:
		if user in users:

			x = users[user]
			f2.writerow([user,xstr(x['name']),xstr(x['company']),xstr(x['email']),xstr(x['bio']).replace('\n',' '),xstr(x['blog']),xstr(x['location'])])
			#f1.write(user+','+xstr(x['name'])+','+xstr(x['company'])+','+xstr(x['email'])+','+xstr(x['bio']).replace('\n',' ')+','+xstr(x['blog'])+','+xstr(x['location'])+'\n')
		else:
			print user