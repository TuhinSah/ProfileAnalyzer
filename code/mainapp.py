import sys
import re
import json
import os
import glob
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import codecs
from github import Github
from LinkedInProfileScraper import *
import getFeat
from prediction import *
from getSimilar import getSim

def getGithubFeat(user):
	g = Github()
	try:
		u = g.get_user(user)
	except:
		print "not found"
		return None
	curuser = u.raw_data
	feat = []
	feat.append(curuser['public_repos'])
	feat.append(curuser['public_gists'])
	feat.append(curuser['followers'])
	feat.append(curuser['following'])
	if curuser['bio']:
		feat.append(1)
	else:
		feat.append(0)
	if curuser['hireable']:
		feat.append(1)
	else:
		feat.append(0)
	if curuser['company']:
		feat.append(1)
	else:
		feat.append(0)
	if curuser['blog']:
		feat.append(1)
	else:
		feat.append(0)
	s = u.get_starred()
	feat.append(len(list(s)))
	o = u.get_orgs()
	feat.append(len(list(o)))
	return feat




def getLinkedInFeat(llink):
	info = scrapePage(llink)
	feat = getFeat.getLinkedInFeat(info)
	return feat


def main(glink, llink):
	gfeat = getGithubFeat(glink.split('/')[-1])
	lfeat = getLinkedInFeat(llink)
	sal = getPredictedSalary(gfeat+lfeat)
	res = getSim(gfeat)
	out = {}
	out['salary'] = sal
	out['similar'] = []
	for r in res:
		out['similar'].append({'githublink':r[0], 'linkedinlink':r[1], 'salary':r[2], 'job':r[3]})
	with open('output.json', 'w') as fp:
		json.dump(out, fp)


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])


