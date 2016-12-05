import requests
from bs4 import BeautifulSoup as bs
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

def getSalary(title, company, location):
	if title:
		q = title
		if company:
			q += ', ' + company
	elif company:
		q = company
	else:
		q = ""

	if location:
		l = location
	else:
		l=""

	payload = {'q1': q, 'l1': l}
	r = requests.get('http://www.indeed.com/salary', params=payload)
	x = bs(r.text, 'html.parser')
	try:
		y = x.find(id='salary_display')
		sal = y.find_all('span', class_='salary')[0].text
	except:
		return -1
	if "No" in sal:
		if company:
			return getSalary(title, None, location)
		else:
			return -1

	#print int(sal)

	return locale.atoi(sal[1:])
