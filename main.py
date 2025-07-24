from scrapers.stepstone import scrape_stepstone
from scrapers.indeed import scrape_indeed
from notifier.email_notifier import send_email

def main():
    keywords = ["Data Analyst", "Data Scientist", "Data Engineer", "ML Engineer", "AI Engineer"]
    location = "Berlin"

    print("Scraping StepStone...")
    stepstone_jobs = scrape_stepstone(keywords, location)

    print("Scraping Indeed...")
    indeed_jobs = scrape_indeed(keywords, location)

    all_jobs = {
        "StepStone": stepstone_jobs,
        "Indeed": indeed_jobs,
    }

    send_email(all_jobs)

if __name__ == "__main__":
    main()

