import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sample careers page for demo
URL = "https://realpython.github.io/fake-jobs/"

headers = {"User-Agent": "Mozilla/5.0"}
job_listings = []

def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="card-content")
    
    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        link = job.find("a")["href"]
        
        job_listings.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Apply Link": link
        })

scrape_page(URL)

# Save to Excel
df = pd.DataFrame(job_listings)
df.to_excel("job_listings.xlsx", index=False)
print("Job listings saved to job_listings.xlsx")
