# WSC Job Search Automation

# Important update
WSC has recently changed its website, so the scraping doesn't work at the moment. Will soon work on an updated version

Working for WSC has long been an aspiration of mine. After missing out on an opportunity to apply for a role I thought was great for me due to reserve duty, I decided to create an automation that would not let me miss the opportunity again.
This Python script automates the process of checking for new job opportunities at WSC Sports' careers page. It uses Selenium to scrape the website for job listings and compares these listings against previously seen ones, stored in a file the script creates. If new job opportunities are found, the script sends an email notification.

# Features
Automated Job Listings Check: Automatically checks the WSC Sports careers page for new job listings.
Email Notifications: Sends an email notification if new job opportunities are detected.
Headless Browser Support: Uses a headless browser to scrape website data, allowing for operation on servers or as a scheduled background task.

# Requirements:
1. Python 3.6+
2. Selenium WebDriver
3. A Gmail account for sending email notifications
4. Chromedriver: Download ChromeDriver matching your Chrome browser's version from the ChromeDriver downloads page and place it in your project directory.

# Configuration:
1. Email Setup: Edit the script to include your email in the SENDER_EMAIL and RECIPIENT_EMAIL fields.
2. Password: The script retrieves the sender's email password from an environment variable (SMTP_WSC_PASSWORD). Ensure this is correctly set in your system.

# Scheduling with Windows Task Scheduler:
1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at 10 AM.
3. For the action, specify the path to your Python executable and add the path to WSC_job_search_automation.py as an argument.
4. Ensure the "Start in" field points to your project directory.

   
# Note
This script is designed for personal use and educational purposes. Be mindful of the terms of service and usage policies of the website being scraped.
