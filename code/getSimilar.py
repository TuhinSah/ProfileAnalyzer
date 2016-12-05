import numpy as np 
import cPickle as pickle 
import operator
import pdb


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
	
	ans = []
	for b in best:
		ans.append(('https://github.com/'+b[0], glsmap[b[0]][0], glsmap[b[0]][1]))
	#pdb.set_trace()	
	#print ans
	return ans


