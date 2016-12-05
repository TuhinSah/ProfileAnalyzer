import cPickle as pickle 

# glsmap = {}
# i = 0
# with open('../data/profilesalaries2.txt', 'r') as f1:
# 	for line in f1:
# 		sp = line.rstrip('\n').split(',')
# 		uid = sp[0]
# 		salary = int(sp[1])
# 		with open('../data/profilepages/'+uid+'.html', 'r') as f2:
# 			x = f2.read()
# 			link = x.split('\n')[-1]
# 			print link
# 			if 'linkedin.com/in/' in link:
# 				glsmap[uid] = (link, salary)

# print len(glsmap)

# pickle.dump(glsmap, open('../data/glsmap.p', 'wb'))
				

glsmap = pickle.load(open('../data/glsmap.p', 'rb'))

sals = {}
with open('../data/searchsalaries2.txt', 'r') as f1:
	for line in f1:
		uid, s = line.rstrip('\n').split(',')
		s = int(s)
		sals[uid] = s
with open('../data/searchmatches.csv', 'r') as f1:
	for line in f1:
		uid, link = line.rstrip('\n').split(',')
		if uid in sals:
			glsmap[uid] = (link, sals[uid])

print len(glsmap)
pickle.dump(glsmap, open('../data/glsmap.p', 'wb'))