import cPickle as pickle
import random
import codecs


users = pickle.load(open('allusersinfo.p', 'rb'))

x = users.items()
random.shuffle(x)
f1=codecs.open('testdata.csv', 'w', 'utf-8')
for user in x:
	if user[1]['type'] != 'User':
		print "Not user"
		continue
	fullname = user[1].get('name')
	if not fullname:
		continue
	names = fullname.split()
	if len(names) == 1:
		firstName = names[0]
		lastName = None
	else:
		firstName = names[0]
		lastName = ' '.join(names[1:])
	print firstName
	print lastName
	if not firstName:
		firstName = '+'
	if not lastName:
		lastName = '+'
	url = 'https://www.linkedin.com/pub/dir/'+firstName+'/'+lastName
	giturl = user[1]['html_url']
	print giturl
	print user[0]
	f1.write(user[0]+','+fullname+','+giturl+','+url+'\n')
	#searchUser(user, firstName, lastName)
	#done.add(user)

f1.close()