#reades in a file of Firstname, Lastname and searches for them on linkedin, 
#storing the search page in a file


import requests
from bs4 import BeautifulSoup as bs
import cPickle as pickle
import random, string
import time
from fake_useragent import UserAgent
from selenium import webdriver
import codecs
import glob

path_to_chromedriver = '/Users/simrat/Downloads/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
signupcount = 0

ua = UserAgent()

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def getUserAgent():
	return ua.random
	#return randomword(15)


def searchUser(username, firstName, lastName):
	global signupcount
	global browser
	if not firstName:
		firstName = '+'
	if not lastName:
		lastName = '+'
	#ua = getUserAgent()
	headers = {
    'User-Agent':  ua
    }
	url = 'https://www.linkedin.com/pub/dir/'+firstName+'/'+lastName
	#print headers
	#input(url)
	#r = requests.get(url, headers=headers)
	browser.get(url)
	print browser.title
	#print r.status_code
	if 'Sign' not in browser.title:
		if 'pub/dir' in browser.current_url:
			with codecs.open('data/searchpages/'+username+'.html', 'w', 'utf-8') as f1:
				f1.write(browser.page_source+'\n')
				f1.write(browser.current_url)
		else:
			with codecs.open('data/profilepages/'+username+'.html', 'w', 'utf-8') as f1:
				f1.write(browser.page_source+'\n')
				f1.write(browser.current_url)
	else:
		signupcount += 1
		if signupcount>5:
			print "RESETTING"
			browser = webdriver.Chrome(executable_path = path_to_chromedriver)
			signupcount = 0


	s = random.random()*10
	print s
	print "Sleeping"
	time.sleep(s)
	#soup = bs(r.text, 'html.parser')


users = pickle.load(open('allusersinfo.p', 'rb'))
f1 = open('nonames.txt', 'a')
f2 = open('notuser.txt', 'a')
files = glob.glob('data/*/*.html')
done = set()
for file in files:
	done.add(file.split('/')[2][:-5])
print done
for user in users:
	if user in done:
		continue
	print len(done)
	print user
	if users[user]['type'] != 'User':
		print "Not user"
		f2.write(user+'\n')
		continue
	fullname = users[user].get('name')
	if not fullname:
		print "No name"
		f1.write(user+'\n')
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
	searchUser(user, firstName, lastName)
	done.add(user)

f1.close()

