import cPickle as pickle 
import json
import glob
from bs4 import BeautifulSoup as bs
import codecs
import pdb
from collections import Counter


def getLinkedInFeat(c):
	commonschools = pickle.load(open('../data/commonschools.p', 'rb'))
	commonloc = pickle.load(open('../data/commonloc.p', 'rb'))
	feat = []
	jobs = 0
	if 'title' in c['current'] and c['current']['title'] != '-':
		jobs += 1
	jobs += len(c['previous'])
	feat.append(jobs)
	skills = len(c['skills'])
	feat.append(skills)

	feat.append(len(c['education']))
	feat.append(len(c['links']))
	feat += addSchoolFeat(c, commonschools)
	feat += addLocFeat(c, commonloc)

	return feat
	
	
def addSchoolFeat(c, commonschools):

	feat = []
	for	school, count in commonschools:
		if school in [x['school'] for x in c['education']]:
			feat.append(1)
		else:
			feat.append(0)
	return feat

def addLocFeat(c, commonloc):
	
	feat = []
	for	loc, count in commonloc:
		if loc == c['locality']:
			feat.append(1)
		else:
			feat.append(0)
	return feat
	#return feat, skillset, c['locality'], schoolset