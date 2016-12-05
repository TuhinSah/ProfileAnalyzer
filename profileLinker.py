import cPickle as pickle 
import json
import glob
from bs4 import BeautifulSoup as bs
import codecs
import pdb

f1 = codecs.open('data/profilematches.txt', 'w', 'utf-8')
f2 = codecs.open('data/notfound.txt', 'w', 'utf-8')


files = glob.glob('data/profilepages/*.html')
needed = []
for file in files:
	needed.append(file.split('/')[2][:-5])

# for uid in needed:
# 	with open('data/profilepages/'+uid+'.html', 'r') as f1:
# 		soup = bs(f1.read(), 'html.parser')

users = pickle.load(open('allusersinfo.p', 'rb'))


with open('data/ProfileData 4.json', 'r') as f3:
	x = json.loads(f3.read())

umap = {}
for y in x:
	if y['name']:
		umap[y['name']] = y

#pdb.set_trace()
print len(umap)
print len(needed)

for uid in needed:
	with open('data/profilepages/'+uid+'.html', 'r') as f3:
		soup = bs(f3.read(), 'html.parser')
	try:
		name = soup.find(id='name').text
	except:
		f2.write(uid+','+users[uid]['name']+',signup?\n')
		continue
	if name in umap:
		f1.write(uid+','+name+'\n')
	else:
		f2.write(uid+','+users[uid]['name']+','+name+'\n')

