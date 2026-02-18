News Headline Scraper 📰
A lightweight Python utility designed to automate the collection of top news headlines from public websites. This project demonstrates basic web scraping techniques using the requests and BeautifulSoup libraries.

🚀 Features
Automated Fetching: Retrieves live HTML data from a target news URL.

Smart Parsing: Extracts text specifically from headline tags (e.g., <h2>).

Data Export: Automatically cleans the text and saves it into a numbered .txt file for easy reading.

🛠️ Tools & Libraries
Python 3.x

Requests: For handling HTTP requests.

BeautifulSoup4: For parsing HTML and navigating the DOM.


Getty Images
Explore
📋 Installation & Setup
Clone the repository (or save the script to your local folder).

Install dependencies using pip:

Bash
pip install requests beautifulsoup4
Run the script:

Bash
python scraper.py
📖 How It Works
The script follows a simple three-step logic:

Request: It sends a "GET" request to the website with a browser-like header.

Parse: BeautifulSoup scans the HTML for specific tags (like <h2> or <span class="title">).

Output: It iterates through the found elements, strips away extra whitespace, and appends them to headlines.txt.

⚠️ Disclaimer
This tool is for educational purposes. Always check a website's robots.txt file and Terms of Service before scraping to ensure you are following their data privacy and crawling policies.