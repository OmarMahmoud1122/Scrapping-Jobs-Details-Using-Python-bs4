# Import libraries
import urllib.request,urllib.parse,urllib.error
import requests
import bs4
import json
import pandas as pd
# Scrapper function takes: job position, job location and required number of pages to scrape 
def scrapper(position,location,num_of_pages):
    # Split job position then convert it to string changing space ' ' to '%20' to fit in the url 
    pos = position.split()
    pos1 = '%20'.join(pos)
    # Same with location
    loc = location.split()
    loc1 = '%20'.join(loc)
    # Create four lists to store values and construct DataFrame
    job_name = []
    Link = []
    company_name = []
    job_type = []
    # Loop through pages
    for i in range(num_of_pages):
        # Access target webpage with desired inputs then get HTML and create beautifulsoup object
        data1 = requests.get(f'https://wuzzuf.net/search/jobs/?a=navbl&filters%5Bcountry%5D%5B0%5D={loc1}&q={pos1}&start={num_of_pages}')
        soup = bs4.BeautifulSoup(data1.text,'html.parser')
        # Acess target tags
        jobs = soup.find_all('div',class_ = 'css-1gatmva e1v1l3u10')
    
        # Loop through tags and extract information then store them in lists
        for job in jobs:
            job_name.append(job.h2.text)
            Link.append(job.h2.a.get('href'))
            company_name.append(job.find('a',class_ = 'css-17s97q8').text[:-1])
            job_type.append(job.find('a' ,class_ = 'css-n2jc4m').text)
    # Construct DataFrame then print it
    df = pd.DataFrame({'job_name': job_name, 'company_name' : company_name, 'job_type':job_type,'Link':Link})
    print(df)
    
# Calling function with inputs
scrapper('data analyst','Egypt',2)