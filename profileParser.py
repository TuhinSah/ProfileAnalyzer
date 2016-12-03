import sys
import re
import json
import os
import glob
from bs4 import BeautifulSoup

if __name__ == "__main__":
	profiles = []
	for f in glob.glob(sys.argv[1] + "*.html"):
		print "Getting data for file " + f
		profilePage = open(f).read()
		soup = BeautifulSoup(profilePage, "html.parser")

		try:
			name = soup.find("h1", { "id" : "name" }).text.strip()
		except:
			name = False
		#print name

		links = []
		try:
			websites = soup.find("tr", { "class" : "websites" }).find_all("a")
			for website in websites:
				links.append(website.get('href'))
		except:
			websites = False
		#for link in links:
			#print link

		jobs = []
		try:
			positions = soup.find_all("li", { "class" : "position" })
		except:
			positions = False

		if positions:
			for position in positions:
				job = {}
				try:
					title = position.find("h4", {"class" : "item-title"}).text.strip()
					job['title'] = title
				except:
					title = False

				try:
					company = position.find("h5", {"class" : "item-subtitle"}).text.strip()
					job['company'] = company
				except:
					company = False

				try:
					location = position.find("span", {"class" : "location"}).text.strip()
					job['location'] = location
				except:
					location = False

				jobs.append(job)
		#print jobs

		skills = []
		try:
			ss = soup.find_all("li", {"class" : "skill"})
		except:
			ss = False

		if ss:
			for s in ss:
				try:
					skill = s.find("span", {"class" : "wrap"}).text.strip()
					skills.append(skill)
				except:
					skill = False
		#print skills

		education = []
		try:
			schools = soup.find_all("li", {"class" : "school"})
		except:
			schools = False

		if schools:
			for s in schools:
				programme = {}
				try:
					school = s.find("h4", {"class" : "item-title"}).text.strip()
					programme['school'] = school
				except:
					school = False

				try:
					course = s.find("h5", {"class" : "item-subtitle"}).find("span", {"class" : "translated translation"}).text.strip()
					programme['course'] = course
				except:
					course = False

				education.append(programme)
		#print education
		profile = {'name': name, 'links': links, 'jobs': jobs, 'skills': skills, 'education': education}
		profiles.append(profile)

	with open('ProileData.json', 'w') as fp:
		json.dump(profiles, fp)
