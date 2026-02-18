import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file):
    # 1. Fetch the HTML content
    # We add a User-Agent header so the site knows we are a browser, not a bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        
        # 2. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <h2> tags (common for headlines)
        # Note: You may need to change 'h2' to 'h3' or a specific class 
        # depending on the website's structure.
        headlines = soup.find_all('h2')
        
        # 3. Save the titles to a .txt file
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, tag in enumerate(headlines, 1):
                clean_text = tag.get_text().strip()
                if clean_text:
                    f.write(f"{i}. {clean_text}\n")
        
        print(f"Success! {len(headlines)} headlines saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    TARGET_URL = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en" # Example: Hacker News
    # For Hacker News, headlines are actually in <span> with class 'titleline'
    # But for a standard news site, <h2> is a great starting point.
    scrape_headlines(TARGET_URL, "headlines.txt")