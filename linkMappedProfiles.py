import json
import codecs
import unicodecsv as csv
import cPickle as pickle 

linkmap = {}
with open('data/ProfileCardData 2.json', 'r') as f1:
	d = json.loads(f1.read())

for u in d:
	url = u['link']
	if url not in linkmap:
		linkmap[url] = []
	linkmap[url].append(u)

print len(linkmap)
pickle.dump(linkmap, open('data/linkmapsearch.p', 'wb'))