import cPickle as pickle
import glob
import pdb
import json
import editdistance
from bs4 import BeautifulSoup as bs


def getSimilarity(uid, user, linid, potmatch):
	score = 0
	#print user
	#print potmatch
	if 'california' in potmatch['country'].lower():
		score += 1
	if user.get('location'):
		ed = editdistance.eval(user['location'], potmatch['country'])
		if ed < 5:
			score += 1
	if user.get('comapany') and user['company'] in potmatch['job']:
		score += 1
	ed = editdistance.eval(uid, linid.split('/')[-1])
	if ed < 5:
		score += 1
	return score


files = glob.glob('data/searchpages/*.html')
needed = []
for file in files:
	needed.append(file.split('/')[2][:-5])
users = pickle.load(open('allusersinfo.p', 'rb'))


with open('data/ProfileCardData 2.json', 'r') as f1:
	res = json.loads(f1.read())

f2 = open('data/matchedrecords.txt', 'a')
threshold = 1
linkmap = pickle.load(open('data/linkmapsearch.p', 'rb'))
for user in needed:
	with open('data/searchpages/'+user+'.html', 'r') as f1:
		soup = bs(f1.read(), 'html.parser')
	links = []
	for link in soup.find_all('a'):
		if link.get('class') and 'public-profile-link' in link['class']:
			links.append(link['href'])
	best = -1
	for link in links:
		if link in linkmap:
			for c in linkmap[link]:
				s = getSimilarity(user, users[user], link, c)
				if s > best:
					best = s
					match = link
	if best >= threshold:
		f2.write(user+','+link+','+str(best)+'\n')



