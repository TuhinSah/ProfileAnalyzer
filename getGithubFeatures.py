import cPickle as pickle 
import glob
import requests


def getGithubFeat(user):
	curuser = users[user]
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
	r = requests.get('https://api.github.com/users/'+user+'/starred/')
	starred = len(r.json())
	feat.append(starred)
	o = requests.get(curuser['organizations_url'])
	org = len(o.json())
	feat.append(org)
	l = requests.get('https://opensourcecontributo.rs/api/user/'+user)
	x = l.json()
	contr = x['eventCount']
	repos = len(x['repos'])
	feat.append(contr)
	feat.append(repos)
	print feat
	return feat



users = pickle.load(open('allusersinfo.p', 'rb'))
try:
	gfeat = pickle.load(open('githubfeatures.p', 'rb'))
except:
	gfeat = {}
files = glob.glob('data/*/*.html')
needed = set()
for file in files:
	needed.add(file.split('/')[2][:-5])
print len(needed)
print len(gfeat)
for user in needed:
	if user not in gfeat:
		print user
		gfeat[user] = getGithubFeat(user)
		if len(gfeat)%50 == 0:
			print len(gfeat)
			pickle.dump(gfeat, open('githubfeatures.p', 'wb'))
