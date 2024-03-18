from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import datetime

# Function to extract job titles
def get_job_titles(url):
    options = Options()
    options.headless = True
    # Update the path to your ChromeDriver
    service = Service('C:\\Users\\user\\Desktop\\Code_Projects\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    try:
        wait = WebDriverWait(driver, 10)
        # Adjusted selector to target the job titles directly
        job_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".comeet-position-name")))
        job_titles = [element.text.strip() for element in job_elements]
    finally:
        driver.quit()

    return job_titles

# Function to check for new job opportunities
def check_new_jobs(url, filepath='seen_jobs.txt'):
    current_jobs = get_job_titles(url)
    try:
        with open(filepath, 'r') as file:
            seen_jobs = file.read().split('\n')
    except FileNotFoundError:
        seen_jobs = []

    new_jobs = [job for job in current_jobs if job not in seen_jobs]

    # Update the seen_jobs file with current job titles
    with open(filepath, 'w') as file:
        for job in current_jobs:
            file.write("%s\n" % job)

    return new_jobs

# Function to send email
def send_email(subject, body, recipient, sender_email, sender_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient, text)
    server.quit()

# Main logic
if __name__ == "__main__":
    WSC_CAREERS_URL = "https://wsc-sports.com/careers/"
    SENDER_EMAIL = "shachar.bloch@gmail.com"
    RECIPIENT_EMAIL = "shachar.bloch@gmail.com"
    SENDER_PASSWORD = os.environ.get('SMTP_WSC_PASSWORD') # Updated the environment variable name
    #print(SENDER_PASSWORD) #debugging
    new_jobs = check_new_jobs(WSC_CAREERS_URL)
    if new_jobs:
        body = "New job opportunities at WSC: \n" + "\n".join(new_jobs)
        send_email("New job opportunity at WSC!", body, RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD)
    else:
        send_email("No new job opportunities at WSC as of today", "No new job opportunities at WSC as of today", RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD)

