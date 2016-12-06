import numpy as np 
import cPickle as pickle 
import operator
import pdb
import json

def isSame(a, b):
	for i in range(0, len(a)):
		if b[i] != a[i]:
			return False
	return True

def getSim(feat):
	ofeat = feat
	#feat = np.array(feat)
	mn, st = pickle.load(open('../data/datanorm.p', 'rb'))
	gfeat = pickle.load(open('../githubfeatures.p', 'rb'))
	glsmap = pickle.load(open('../data/glsmap.p', 'rb'))
	#pdb.set_trace()
	feat = (feat-mn)/st
	scores = []
	for uid in glsmap:
		scores.append((uid, np.dot(feat, (gfeat[uid]-mn)/st)))
		
		#if uid == 'bloudraak':
			#print np.dot(feat, (gfeat[uid]-mn)/st)
	#lprint scores
	best = sorted(scores, key=operator.itemgetter(1), reverse=True)[:3]
	
	
	with open('../data/ProfileData 5.json', 'r') as f3:
		x = json.loads(f3.read())

	umap = {}
	for y in x:
		if y['name']:
			umap[y['name']] = y

	with open('../data/ProfileCardData 2.json', 'r') as f3:
		xs = json.loads(f3.read())

	umaps = {}
	for y in xs:
		if y['link']:
			umaps[y['link']] = y
	pmatch = {}
	with open('../data/profilematches.txt', 'r') as f1:
		for line in f1:
			sp = line.rstrip('\n').split(',')
			uid = sp[0]
			uname = ','.join(sp[1:]) 
			pmatch[uid] = uname
	jobs = []
	for b in best:
		uid = b[0]
		if uid in pmatch:
			current = umap[pmatch[uid]]['current']
			print current
			if 'title' in current:
				if 'company' in current:
 					job = current['title'] + ', ' + current['company']
 				else:
 					job = current['title']
			else:
				if 'company' in current:
					job = current['company']
				else:
					job = ""
		else:
			current = umaps[glsmap[uid][0]]['current']
			job = current
		jobs.append(job)

	ans = []
	for i in range(3):
		b = best[i]
		ans.append(('https://github.com/'+b[0], glsmap[b[0]][0], glsmap[b[0]][1], jobs[i]))



	#pdb.set_trace()	
	#print ans
	return ans


