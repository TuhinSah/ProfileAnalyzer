import sys
import re
import json
import os
import glob
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import codecs

path_to_chromedriver = '/Users/simrat/Downloads/chromedriver'

def scrapePage(llink):
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.get(llink)
    profilePage = driver.page_source

    soup = BeautifulSoup(profilePage, "html.parser")

    try:
        name = soup.find("h1", { "id" : "name" }).text.strip()
    except:
        name = False

    try:
        locality = soup.find("span", { "class" : "locality" }).text.strip()
    except:
        locality = False

    links = []
    try:
        websites = soup.find("tr", { "class" : "websites" }).find_all("a")
        for website in websites:
            links.append(website.get('href'))
    except:
        websites = False

    current = {}
    try:
        position = soup.find("li", {"data-section" : "currentPositionsDetails"})
    except:
        position = False

    if position:
        try:
            title = position.find("h4", {"class" : "item-title"}).text.strip()
            current['title'] = title
        except:
            title = False

        try:
            company = position.find("h5", {"class" : "item-subtitle"}).text.strip()
            current['company'] = company
        except:
            company = False

        try:
            location = position.find("span", {"class" : "location"}).text.strip()
            current['location'] = location
        except:
            location = False

    if not locality:
        if 'location' in current:
            locality = current['location']
        else:
            locality = '-'

    jobs = []
    try:
        positions = soup.find_all("li", { "data-section" : "pastPositionsDetails" })
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
    profile = {'name': name, 'links': links, 'locality': locality,'current': current, 'previous': jobs, 'skills': skills, 'education': education}
    return profile
    #with open('ProileData.json', 'w') as fp:
       # json.dump(profile, fp)
