SEC 10-K Data Scraper
This project is a Python-based data scraper that automatically downloads SEC 10-K reports for companies listed in the S&P 500. The 10-K reports provide valuable financial information for analysis, such as revenue, profit, assets, and more. The script fetches the reports from the SEC EDGAR database, processes the data, and stores it in a structured format for further analysis.

Features
Automatically download 10-K reports for multiple companies.
Filter for specific forms (e.g., 10-K).
Download data as Excel files for easy access.
Multi-threading support for faster downloads.
Error handling for missing or incorrect CIK numbers.
Requirements
Before running the script, ensure you have the following dependencies installed:

Python 3.x
requests
rich
edgarpython
beautifulsoup4
pandas
You can install these dependencies using pip:

bash
Copy code
pip install requests rich edgarpython beautifulsoup4 pandas
How It Works
CSV Input: The script reads a CSV file (sp500.csv) containing company information, including their ticker symbols and CIK numbers.
Fetching Submissions: It connects to the SEC EDGAR API to fetch the company's filings and filter out the 10-K reports.
Download Reports: The script then downloads the reports as Excel files into individual company folders.
Output: All reports are saved in the Output directory under subfolders named after each company.
Usage
Clone the Repository

Open your terminal or command prompt and clone the repository using the URL you provided:

bash
Copy code
git clone https://github.com/jayendra-jamadar/Web-Scrapping-Sec-Website.git
cd Web-Scrapping-Sec-Website
Add the README.md File

Create or replace the README.md file in the cloned repository directory with the following content:

markdown
Copy code
# SEC 10-K Data Scraper

This project is a Python-based data scraper that automatically downloads SEC 10-K reports for companies listed in the S&P 500. The 10-K reports provide valuable financial information for analysis, such as revenue, profit, assets, and more. The script fetches the reports from the [SEC EDGAR database](https://www.sec.gov/edgar/searchedgar/companysearch.html), processes the data, and stores it in a structured format for further analysis.

## Features

- Automatically download 10-K reports for multiple companies.
- Filter for specific forms (e.g., 10-K).
- Download data as Excel files for easy access.
- Multi-threading support for faster downloads.
- Error handling for missing or incorrect CIK numbers.
  
## Requirements

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `requests`
- `rich`
- `edgarpython`
- `beautifulsoup4`
- `pandas`

You can install these dependencies using pip:

```bash
pip install requests rich edgarpython beautifulsoup4 pandas
How It Works
CSV Input: The script reads a CSV file (sp500.csv) containing company information, including their ticker symbols and CIK numbers.
Fetching Submissions: It connects to the SEC EDGAR API to fetch the company's filings and filter out the 10-K reports.
Download Reports: The script then downloads the reports as Excel files into individual company folders.
Output: All reports are saved in the Output directory under subfolders named after each company.
Usage
1. Clone the Repository
bash
Copy code
git clone https://github.com/jayendra-jamadar/Web-Scrapping-Sec-Website.git
cd Web-Scrapping-Sec-Website
2. Prepare Your CSV File
Make sure you have a CSV file named sp500.csv in the root directory. The file should include the following columns:

Ticker – Company’s stock ticker symbol (e.g., AAPL for Apple).
CIK – The company’s Central Index Key (CIK) number, which is used by the SEC to identify companies.
3. Run the Script
Once everything is set up, simply run the Python script:

bash
Copy code
python sec_10k_scraper.py
This will start downloading the 10-K reports for each company listed in the CSV file.

4. Customizing the Script
You can modify the script to fetch different forms (e.g., 10-Q) or download reports for a different range of years. The script can be adjusted to suit your specific needs.

Output Structure
The reports are saved in an Output folder, organized by company name:

Copy code
Output/
├── Apple/
│   ├── 1234567890.xlsx
│   └── 0987654321.xlsx
├── Microsoft/
│   ├── 1122334455.xlsx
│   └── 5566778899.xlsx
Each file corresponds to a 10-K report in .xlsx format, which can be opened in Excel or analyzed with other tools.

Error Handling
The script handles missing 10-K reports by skipping them and logging the errors.
It also prints out errors for invalid CIK numbers if they are found in the CSV file.
Performance Optimization
The script uses the rich library to provide progress bars and detailed logging.
Multithreading can be added to further improve download speeds.
