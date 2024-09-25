from csv import reader
from os import mkdir, path
from edgarpython.exceptions import InvalidCIK
from edgarpython.secapi import getSubmissionsByCik, getXlsxUrl
from requests import get
from rich.progress import track

def download(url, filename):
    resp = get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
        },
    )
    with open(filename, "wb") as file:
        file.write(resp.content)

# Read the CSV file containing company data
with open("e:/notes/SEM-3/finance/sp500.csv", encoding="utf-8") as file:
    csv = reader(file)
    companies = list(csv)[1:]

# Create the main output directory if it doesn't exist
if not path.exists("Output"):
    mkdir("Output")

# Process each company from the CSV
for company in track(companies):
    output_dir = f"Output/{company[1]}"
    
    # Create a directory for the company if it doesn't exist
    if not path.exists(output_dir):
        mkdir(output_dir)
    else:
        print(f"Directory '{output_dir}' already exists.")
    
    try:
        # Fetch submissions for the company
        submissions = getSubmissionsByCik(company[6])
        selected = []
        
        # Filter for 10-K submissions
        for submission in submissions:
            if submission.form == "10-K":
                selected.append(submission)
        
        print(f"Found {len(selected)} 10-K for {company[1]}")
        downloads = []
        missed = 0
        
        # Collect download URLs for the 10-K reports
        for submission in selected:
            try:
                downloads.append(getXlsxUrl(company[6], submission.accessionNumber))
            except FileNotFoundError:
                missed += 1
                continue
        
        print(f"{len(downloads)} reports to be downloaded for {company[6]} [missed {missed}]")
        total = len(downloads)
        done = 0
        
        # Download each report
        for downloadUrl in downloads:
            download(
                downloadUrl,
                f"{output_dir}/{downloadUrl.split('/')[-2]}.xlsx",
            )
            done += 1
            print(f"Downloaded [{done}/{total}]")

    except InvalidCIK:
        print("Failed for " + company[1])
        continue
