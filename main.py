from scrapers.stepstone import scrape_stepstone
from scrapers.indeed import scrape_indeed
from notifier.email_notifier import send_email

def main():
    keywords = ["Data Analyst", "Data Engineer", "Data Scientist", "AI Engineer", "ML Engineer"]
    location = "Berlin"

    jobs_stepstone = scrape_stepstone(keywords, location)
    jobs_indeed = scrape_indeed(keywords, location)

    all_jobs = jobs_stepstone + jobs_indeed
    if all_jobs:
        send_email(all_jobs)
    else:
        print("No new jobs found today.")

if __name__ == "__main__":
    main()
