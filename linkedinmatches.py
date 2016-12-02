#reades in a file of Firstname, Lastname and searches for them on linkedin, 
#storing the search page in a file

import requests
from bs4 import BeautifulSoup as bs
import cPickle as pickle
import random, string
import time
from fake_useragent import UserAgent

ua = UserAgent()

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def getUserAgent():
	return ua.random
	#return randomword(15)


def searchUser(username, firstName, lastName):
	if not firstName:
		firstName = '+'
	if not lastName:
		lastName = '+'
	ua = getUserAgent()
	headers = {
    'User-Agent':  ua
    }
	url = 'https://www.linkedin.com/pub/dir/'+firstName+'/'+lastName
	print headers
	input(url)
	r = requests.get(url, headers=headers)
	print r.status_code
	if r.status_code == 200:
		if 'pub/dir' in r.url:
			with open('data/searchpages/'+username+'.html', 'w') as f1:
				f1.write(r.text)
		else:
			with open('data/profilepages/'+username+'.html', 'w') as f1:
				f1.write(r.text)
	s = random.random()*60
	print s
	print "Sleeping"
	time.sleep(s)
	#soup = bs(r.text, 'html.parser')


users = pickle.load(open('allusersinfo.p', 'rb'))
f1 = open('nonames.txt', 'a')
for user in users:
	print user
	if 'name' not in users[user]:
		print "No name"
		f1.write(user+'\n')
		continue
	names = users[user]['name'].split()
	if len(names) == 1:
		firstName = names[0]
		lastName = None
	else:
		firstName = names[0]
		lastName = ' '.join(names[1:])
	print firstName
	print lastName
	searchUser(user, firstName, lastName)
f1.close()

