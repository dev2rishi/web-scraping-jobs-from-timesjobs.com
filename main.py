from bs4 import BeautifulSoup
import requests
import time

print('\nWeb Scraping Jobs from timesjobs.com  \n')
print('Put some skill that you are not familiar with')
unfamiliar_skills = input('> ')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
  html_text = ('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
  soup = BeautifulSoup(requests.get(html_text).content, 'html.parser')

  jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

  for index, job in enumerate (jobs):
   published_date = job.find('span', class_='sim-posted').span.text

   if 'few' in published_date:
 
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    directlink_to_job = job.header.h2.a['href']
    
    if unfamiliar_skills not in skills:
     with open(f'posts{index}.txt', 'w') as f:
      f.write(f"Company Name:- {company_name.strip()} \n") 
      f.write(f"Required Skills:- {skills.strip()} \n")
      f.write(f"DirectLink to Job:- {directlink_to_job} \n")
     print(f'File Saved {index}') 

if __name__ == '__main__':
    while True:
      find_jobs()
      time_wait = 1
      print(f'Waiting {time_wait} minutes')
      time.sleep(time_wait * 60)
