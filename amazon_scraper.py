import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time
import smtplib
import os

# Configuration
URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}
DATA_FILE = 'AmazonWebScraperDataset.csv'
PRICE_THRESHOLD = 15.0

def get_product_info(url):
    """Extracts title and price from an Amazon product page."""
    try:
        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Amazon often changes IDs, using multiple selectors for robustness
        title_elem = soup.find(id='productTitle')
        price_elem = soup.find(id='priceblock_ourprice') or soup.find(class_='a-offscreen')
        
        if not title_elem or not price_elem:
            print("Error: Could not find title or price on the page.")
            return None, None
            
        title = title_elem.get_text().strip()
        price_str = price_elem.get_text().strip()
        
        # Clean price string (e.g., "$16.99" -> 16.99)
        price = float(price_str.replace('$', '').replace(',', ''))
        
        return title, price
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return None, None

def save_to_csv(title, price):
    """Appends the scraped data to a CSV file."""
    today = datetime.date.today().strftime('%Y-%m-%d')
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    file_exists = os.path.isfile(DATA_FILE)
    
    with open(DATA_FILE, 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)
    print(f"Data saved: {title} - ${price} on {today}")

def send_mail(title, price):
    """Sends an email alert if the price drops below the threshold."""
    # Note: Requires valid credentials and app password for Gmail
    sender_email = 'FatmaTheAnalyst95@gmail.com'
    receiver_email = sender_email
    password = 'your_app_password_here' # Use environment variables for security
    
    subject = f"Price Drop Alert: {title} is now ${price}!"
    body = f"The item you've been tracking has dropped below ${PRICE_THRESHOLD}. Buy it now: {URL}"
    msg = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def run_scraper():
    """Main execution loop for the scraper."""
    print("Starting Amazon Web Scraper...")
    title, price = get_product_info(URL)
    
    if title and price:
        save_to_csv(title, price)
        if price < PRICE_THRESHOLD:
            # send_mail(title, price) # Uncomment to enable email alerts
            print(f"Price alert! {price} is below {PRICE_THRESHOLD}")
    else:
        print("Scraping failed. Check URL or headers.")

if __name__ == "__main__":
    # Run once for demonstration
    run_scraper()
    
    # To run periodically (e.g., every 24 hours):
    # while True:
    #     run_scraper()
    #     time.sleep(86400)
