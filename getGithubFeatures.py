import cPickle as pickle 
import glob
import requests
import getpass
from github import Github

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
	try:
		u = g.get_user(user)
	except:
		print "not found"
		feat.append(-1)
		feat.append(-1)
		print feat 
		return feat
	s = u.get_starred()
	feat.append(len(list(s)))
	o = u.get_orgs()
	feat.append(len(list(o)))
	# r = requests.get('https://api.github.com/users/'+user+'/starred/', auth=('the-archer', password))
	# starred = len(r.json())
	# if 'message' in r.json():
	# 	print r.json()
	# 	pickle.dump(gfeat, open('githubfeatures.p', 'wb'))
	# 	a = raw_input()
	# feat.append(starred)
	# o = requests.get(curuser['organizations_url'], auth=('the-archer', password))
	# org = len(o.json())
	# if 'message' in o.json():
	# 	print o.json()
	# 	pickle.dump(gfeat, open('githubfeatures.p', 'wb'))
	# 	a = input()
	# feat.append(org)
	# # l = requests.get('https://opensourcecontributo.rs/api/user/'+user)
	# x = l.json()
	# contr = x['eventCount']
	# repos = len(x['repos'])
	# feat.append(contr)
	# feat.append(repos)
	print feat
	return feat


password = getpass.getpass("Enter password for the-archer:")
g = Github("the-archer", password)
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
i = 0
for user in needed:
	if user not in gfeat:
		print user
		gfeat[user] = getGithubFeat(user)
		if len(gfeat)%50 == 0:
			print len(gfeat)
			pickle.dump(gfeat, open('githubfeatures.p', 'wb'))
	elif gfeat[user][8] == -1:
		print user
		i += 1
		gfeat[user] = getGithubFeat(user)
		if i%20 == 0:
			print "dumping"
			pickle.dump(gfeat, open('githubfeatures.p', 'wb'))


pickle.dump(gfeat, open('githubfeatures.p', 'wb'))
	
