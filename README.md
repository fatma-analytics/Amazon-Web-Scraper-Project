# 🛒 Amazon Web Scraper: Automated Price Tracking & Alerts

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9+-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2.25+-yellow.svg)](https://requests.readthedocs.io/)

> **"Never miss a deal again."**
> 
> This project is a robust Python-based web scraper designed to track Amazon product prices automatically. It extracts product titles and prices, stores them in a structured CSV format with timestamps, and can send email alerts when prices drop below a specified threshold.

---

## 🚀 Key Features
- **Automated Scraping**: Extracts real-time product data using `BeautifulSoup` and `Requests`.
- **Price Tracking**: Appends data to a persistent CSV file for historical price analysis.
- **Email Alerts**: Integrated `smtplib` functionality to notify users when a target price is reached.
- **Data Cleaning**: Robust string manipulation to handle currency symbols and whitespace.
- **Robust Headers**: Uses custom User-Agents to mimic browser behavior and avoid anti-scraping measures.

---

## 🛠️ Technical Stack
- **Language**: `Python`
- **Libraries**: 
  - `BeautifulSoup4`: For parsing HTML content.
  - `Requests`: For handling HTTP requests.
  - `Pandas`: For data manipulation and CSV handling.
  - `smtplib`: For automated email notifications.
  - `datetime` & `time`: For timestamping and scheduling.

---

## 📂 Project Structure
- `amazon_scraper.py`: Refactored, modular Python script for production-ready scraping.
- `Amazon Web Scraper Project.ipynb`: Original Jupyter Notebook with step-by-step development and testing.
- `AmazonWebScraperDataset.csv`: The generated dataset containing historical price data.
- `Amazon Web Scraper Project.pdf`: Exported version of the development process.

---

## ⚙️ Installation & Usage

### 1. Prerequisites
Ensure you have Python installed, then install the required libraries:
```bash
pip install beautifulsoup4 requests pandas
```

### 2. Configuration
Open `amazon_scraper.py` and update the following:
- `URL`: The Amazon product link you want to track.
- `PRICE_THRESHOLD`: Your target price for email alerts.
- `sender_email` & `password`: (Optional) Your Gmail credentials for alerts (use App Passwords for security).

### 3. Execution
Run the scraper manually:
```bash
python amazon_scraper.py
```
To run it automatically every 24 hours, uncomment the `while` loop in the `if __name__ == "__main__":` block.

---

## 📊 Future Enhancements
- [ ] **Multi-Product Tracking**: Support for a list of URLs.
- [ ] **Data Visualization**: Integrate `Matplotlib` or `Seaborn` to generate price trend graphs.
- [ ] **Cloud Deployment**: Run the scraper on a cloud server (e.g., AWS, Heroku) for 24/7 monitoring.
- [ ] **Proxy Support**: Implement rotating proxies to handle large-scale scraping.

---

## ✍️ Author
**Fatma Hammami**  
*Data Analyst & Python Developer*

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
