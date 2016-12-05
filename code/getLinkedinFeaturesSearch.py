import cPickle as pickle 
import json
import glob
from bs4 import BeautifulSoup as bs
import codecs
import pdb
from collections import Counter
from sklearn.metrics import r2_score


def getLinkedInFeat(uname):
	feat = []
	c = umap[uname]
	jobs = 0
	#if 'title' in c['current'] and c['current']['title'] != '-':
	if c['current'] != '-':
		jobs += 1
	jobs += len(c['previous'])
	feat.append(jobs)
	#skills = len(c['skills'])
	feat.append(-1)

	feat.append(len(c['education']))
	feat.append(-1)
	#feat.append(len(c['links']))
	print feat
	# skillset = Counter(c['skills'])
	schools = set()
	for ed in c['education']:
		schools.add(ed)
	schoolset = Counter(schools)
	return feat, schoolset, c['country']


def addSkillFeat(uname, commonskills):
	c = umap[uname]
	feat = []
	for	skill, count in commonskills:
		if skill in c['skills']:
			feat.append(1)
		else:
			feat.append(0)
	return feat

def addSchoolFeat(uname, commonschools):
	c = umap[uname]
	feat = []
	for	school, count in commonschools:
		if school in c['education']:
			feat.append(1)
		else:
			feat.append(0)
	return feat


def addLocFeat(uname, commonloc):
	c = umap[uname]
	feat = []
	for	loc, count in commonloc:
		if loc == c['country']:
			feat.append(1)
		else:
			feat.append(0)
	return feat

with open('../data/ProfileCardData 2.json', 'r') as f3:
	x = json.loads(f3.read())

umap = {}
for y in x:
	if y['link']:
		umap[y['link']] = y

lfeat = pickle.load(open('../data/linkedinfeat.p', 'rb'))
allskills = Counter()
allschools = Counter()
locations = []
with codecs.open('../data/searchmatches.csv', 'r', 'utf-8') as f1:
	for line in f1:
		sp = line.rstrip('\n').split(',')
		uid = sp[0]
		uname = ','.join(sp[1:])
		print uid
		lfeat[uid], sch, loc = getLinkedInFeat(uname)
		#allskills  +=  ss
		allschools += sch
		locations.append(loc)
# print allskills.most_common(50)
# print len(allskills)
# commonskills = allskills.most_common(50)

commonloc = Counter(locations).most_common(10)
print commonloc

commonschools = allschools.most_common(50)
print commonschools
a = raw_input()

# with codecs.open('../data/profilematches.txt', 'r', 'utf-8') as f1:
# 	for line in f1:
# 		sp = line.rstrip('\n').split(',')
# 		uid = sp[0]
# 		uname = ','.join(sp[1:])
# 		print uid
# 		lfeat[uid] += addSkillFeat(uname, commonskills)
# 		print lfeat[uid]
# 		#allskills  +=  ss

with codecs.open('../data/searchmatches.csv', 'r', 'utf-8') as f1:
	for line in f1:
		sp = line.rstrip('\n').split(',')
		uid = sp[0]
		uname = ','.join(sp[1:])
		print uid
		lfeat[uid] += addSchoolFeat(uname, commonschools)
		print lfeat[uid]
		#allskills  +=  ss

with codecs.open('../data/searchmatches.csv', 'r', 'utf-8') as f1:
	for line in f1:
		sp = line.rstrip('\n').split(',')
		uid = sp[0]
		uname = ','.join(sp[1:])
		print uid
		lfeat[uid] += addLocFeat(uname, commonloc)
		print lfeat[uid]

pickle.dump(lfeat, open('../data/linkedinfeat.p', 'wb'))

