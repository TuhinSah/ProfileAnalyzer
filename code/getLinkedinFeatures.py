import cPickle as pickle 
import json
import glob
from bs4 import BeautifulSoup as bs
import codecs
import pdb

def getLinkedInFeat(uname):
	feat = []
	c = umap[uname]
	jobs = 0
	if 'title' in c['current'] and c['current']['title'] != '-':
		jobs += 1
	jobs += len(c['previous'])
	feat.append(jobs)
	skills = len(c['skills'])
	feat.append(skills)
	feat.append(len(c['education']))
	feat.append(len(c['links']))
	print feat
	return feat




with open('../data/ProfileData 5.json', 'r') as f3:
	x = json.loads(f3.read())

umap = {}
for y in x:
	if y['name']:
		umap[y['name']] = y

lfeat = {}

with codecs.open('../data/profilematches.txt', 'r', 'utf-8') as f1:
	for line in f1:
		sp = line.rstrip('\n').split(',')
		uid = sp[0]
		uname = ','.join(sp[1:])
		print uid
		lfeat[uid] = getLinkedInFeat(uname)

pickle.dump(lfeat, open('../data/linkedinfeat.py', 'wb'))

