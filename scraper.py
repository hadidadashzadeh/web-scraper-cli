# scraper.py

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os

def scrape_jobs(tag, output_format="json"):
    url = f"https://remoteok.com/remote-{tag}-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to fetch jobs. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("tr", class_="job")

    jobs = []
    for job in job_elements:
        try:
            title = job.find("h2").get_text(strip=True)
            company = job.find("h3").get_text(strip=True)
            link = "https://remoteok.com" + job['data-href']
            date = job.find("time")['datetime'] if job.find("time") else "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "link": link,
                "date": date
            })
        except Exception as e:
            continue  # skip malformed entries

    if not os.path.exists("output"):
        os.mkdir("output")

    output_file = f"output/jobs_{tag}.{output_format}"

    if output_format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2)
    else:  # CSV
        df = pd.DataFrame(jobs)
        df.to_csv(output_file, index=False)

    print(f"✅ {len(jobs)} jobs saved to {output_file}")
