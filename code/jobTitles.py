import cPickle as pickle 
import json
import glob
from bs4 import BeautifulSoup as bs
import codecs
import pdb
from indeedsalary import *
import time

done = set()
# with codecs.open('../data/profilesalaries.txt', 'r', 'utf-8') as f1:
# 	for line in f1:
# 		done.add(line.split(',')[0])


f2 = codecs.open('../data/searchsalaries.txt', 'a', 'utf-8')


with open('../data/ProfileCardData 2.json', 'r') as f3:
	x = json.loads(f3.read())

umap = {}
for y in x:
	if y['link']:
		umap[y['link']] = y

atc = set()

with codecs.open('../data/searchmatches.csv', 'r', 'utf-8') as f1:
	for line in f1:
		sp= line.rstrip('\n').split(',')
		uid = sp[0]
		if uid in done:
			continue
		uname = ','.join(sp[1:])
		title = 'software'
		company = None
		if 'current' in umap[uname]:
			title = umap[uname]['current']
			# if 'title' in umap[uname]['current']:
			# 	title = umap[uname]['current']['title']
			# if 'company' in umap[uname]['current']:
			#  	company = umap[uname]['current']['company']
		print title
		print company
		print umap[uname]['country']
		sal = getSalary(title, company, umap[uname]['country'])
		f2.write(uid+','+str(sal)+'\n')
		print uid
		print sal
		time.sleep(1)
			#atc.add(umap[uname]['current']['title'])
			#x = len(atc)
			#atc.add((umap[uname]['current']['title']+','+umap[uname]['current']['company'], umap[uname]['locality']))
			#y = len(atc)
			#if x == y:
				#print(umap[uname]['current']['title']+','+umap[uname]['current']['company'], umap[uname]['locality'])
		#except:
			#continue
		#f2.write(uid+'\t'+umap[uname]['current']['title']+','+umap[uname]['current']['company'] + 
			#'\t'+umap[uname]['locality']+'\n')

#print (atc)
#for a in atc:
	#f2.write(a[0]+'\t'+a[1]+'\n')
