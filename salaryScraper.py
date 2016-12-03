import time
import json
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

username = "" # your email here
password = "" # your password here

class Salary:
    def __init__(self, jobTitle, company, meanPay, city):
        self.jobTitle = jobTitle
        self.company = company
        self.meanPay = meanPay
        self.city = city
    #enddef

def obj_dict(obj):
    return obj.__dict__
#enddef

def json_export(data, cityName, title):
    jsonFile = open("Data/" + cityName + title + ".json", "w+")
    jsonFile.write(json.dumps(data, indent=4, separators=(',', ': '), default=obj_dict))
    jsonFile.close()
#enddef

def init_driver():
    driver = webdriver.Chrome(executable_path = "./chromedriver")
    driver.wait = WebDriverWait(driver, 10)
    return driver
#enddef

def login(driver, username, password):
    driver.get("http://www.glassdoor.com/profile/login_input.htm")
    try:
        user_field = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "username")))
        pw_field = driver.find_element_by_class_name("signin-password")
        login_button = driver.find_element_by_id("signInBtn")
        user_field.send_keys(username)
        user_field.send_keys(Keys.TAB)
        time.sleep(1)
        pw_field.send_keys(password)
        time.sleep(1)
        login_button.click()
    except TimeoutException:
        print("TimeoutException! Username/password field or login button not found on glassdoor.com")
#enddef

def search(driver, city, title):
    driver.get("https://www.glassdoor.com/Salaries/index.htm")
    try:
        search_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "showHH")))
        time.sleep(25)
        title_field = driver.find_element_by_id("KeywordSearch")
        city_field = driver.find_element_by_id("LocationSearch")
        title_field.send_keys(title)
        title_field.send_keys(Keys.TAB)
        time.sleep(5)
        city_field.send_keys(city)
        city_field.send_keys(Keys.RETURN)
        time.sleep(5)
    except TimeoutException:
        print("TimeoutException! city/title field or search button not found on glassdoor.com")
#enddef

def parse_salaries_HTML(salaries, data, city):
    for salary in salaries:
        jobTitle = "-"
        company = "-"
        meanPay = "-"
        jobTitle = salary.find("a", { "class" : "jobTitle"}).getText().strip()
        company = salary.find("div", { "class" : "i-emp"}).getText().strip()
        try:
            meanPay = salary.find("div", { "class" : "meanPay"}).find("strong").getText().strip()
        except:
            meanPay = 'xxx'
        r = Salary(jobTitle, company, meanPay, city)
        data.append(r)
    #endfor
    return data
#enddef

def get_data(driver, URL, city, data, refresh, startPage=1):
    print "\nPage " + str(startPage)
    if (refresh):
        driver.get(URL)
        print "Getting " + URL
        time.sleep(2)
    try:
        next_btn = driver.find_element_by_class_name("next")
        next_link = next_btn.find_element_by_css_selector("a").get_attribute('href')
    except:
        next_btn = False
        next_link = False
    #endif
    time.sleep(2)
    HTML = driver.page_source
    soup = BeautifulSoup(HTML, "html.parser")
    try:
        salaries = soup.find("div", { "class" : ["salaryChartModule"] }).find_all("div", { "class" : ["salaryRow"] })
    except:
        salaries = False
    if (salaries):
        data = parse_salaries_HTML(salaries, data, city)
        print "Page " + str(startPage) + " scraped."
        if (next_link):
            get_data(driver, next_link, city, data, True, startPage + 1)
    else:
        print "No data available for", city
    #endif
    return data
#enddef

if __name__ == "__main__":
    driver = init_driver()
    time.sleep(3)
    print "Logging into Glassdoor account ..."
    login(driver, username, password)
    time.sleep(10)
    # search(driver, city, title)
    print "\nStarting data scraping ..."
    city_list = open("cities.txt").read().splitlines()
    title_list = open("titles.txt").read().splitlines()
    data_out = []
    for city in city_list:
        for title in title_list:
            search(driver, city, 'Data Scientist')
            appendable = get_data(driver, driver.current_url, city, [], False, 1)
            print "\nExporting data to " + city + ".json"
            if appendable:
                data_out.append(appendable)
                json_export(appendable, city, title)
    if data_out:
        json_export(data_out, 'allcities', '')
    driver.quit()
#endif
