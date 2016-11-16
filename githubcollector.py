from github import Github
import getpass
import cPickle as pickle
from time import sleep
import traceback


def paginateAndGetUsers(search):
	users = set()
	totalCount = search.totalCount
	page = 0
	totalPages = totalCount/float(30)
	while page<totalPages:
		try:
			y = search.get_page(page)
			users |= set(y)
			print len(users)
			page += 1
		except:
			traceback.print_exc()
			print "Sleeping"
			sleep(60)
	print len(users)
	return users

def getUserObjects(g, location):
	allusers = set()
	flag = True
	while flag:
		try:
			search = g.search_users('location:'+location+' repos:>100')
			flag = False
			allusers |= paginateAndGetUsers(search)
		except Exception as e:
			traceback.print_exc()
			print "Sleeping"
			sleep(60)
	print len(allusers)
	for repo in range(100, 20, -1):
		print repo
		print len(allusers)
		flag = True
		while flag:
			try:
				search = g.search_users('location:'+str(location)+' repos:'+str(repo))
				allusers |= paginateAndGetUsers(search)
				flag = False
			except:
				traceback.print_exc()
				print "Sleeping"
				sleep(60)
		

	return allusers



def getEachUserInfo(allusers):
	try:
		allusersinfo = pickle.load(open('allusersinfo.p', 'rb'))
	except:
		allusersinfo = {}
	for user in allusers:
		if user.login not in allusersinfo:
			try:
				allusersinfo[user.login] = user.raw_data
				print len(allusersinfo)
				if len(allusersinfo)%100 == 0:
					pickle.dump(allusersinfo, open('allusersinfo.p', 'wb'))
			except:
				traceback.print_exc()
				print "Sleeping"
				sleep(60)














password = getpass.getpass("Enter password for the-archer:")
g = Github("the-archer", password)
#allusers = getUserObjects(g, 'CA')
#pickle.dump(allusers, open('allusers2.p', 'wb'))
allusers = pickle.load(open('CAusers.p', 'rb'))
getEachUserInfo(allusers)