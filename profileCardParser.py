import sys
import re
import json
from bs4 import BeautifulSoup

def obj_dict(obj):
    return obj.__dict__

class Profile:
    def __init__(self, name, link, country, industry, current, *previous):
        self.name = name
        self.link = link
        self.country = country
        self.industry = industry
        self.current = current
        self.previous = previous or []

def json_export(data, name):
    jsonFile = open(name + ".json", "w+")
    jsonFile.write(json.dumps(data, indent=4, separators=(',', ': '), default=obj_dict))
    jsonFile.close()

if __name__ == "__main__":
	searchPage = open(sys.argv[1]).read()
	soup = BeautifulSoup(searchPage, "html.parser")
	
	name = soup.find("div", { "class" : "profile-card" }).find("div", { "class" : "content" }).find("h3").find("a").text.strip()
	
	profiles = []

	try:
		profileCards = soup.find_all("div", { "class" : ["profile-card"] })
	except:
		profileCards = False

	for profileCard in profileCards:
		link = '-'
		country = '-'
		industry = '-'
		current = '-'
		previous = []

		try:
			link = profileCard.find("a").get('href')
		except:
			link = False

		try:
			basic = profileCard.find("dl", { "class" : "basic"}).find_all("dd")
			country = basic[0].text
			industry = basic[1].text
		except:
			basic = False

		try:
			jobs = profileCard.find("tbody").find_all("td")
			currentJob = jobs[0].text

			pastJobs = jobs[1].text.split(', ')
			cut = ''
			for pastJob in reversed(pastJobs):
				if 'at' not in pastJob:
					cut = cut + ', ' + pastJob
				else:
					if cut is not '':
						pastJob = pastJob + cut
					previous.append(pastJob)
		except:
			jobs = False

		profile = Profile(name, link, country, industry, current, previous)
		if profile:
			profiles.append(profile)

	if profiles:
		json_export(profiles, name)
