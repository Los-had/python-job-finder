import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(site, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
posted_time = job.find('span', class_ = 'sim-posted').text
print(f'Company name: {company}\nRequired skills: {skills}\n {posted_time}')