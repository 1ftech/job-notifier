from scrapers.stepstone import scrape_stepstone
from scrapers.indeed import scrape_indeed
# from scrapers.linkedin import scrape_linkedin  # if implemented
from notifier.email_notifier import send_email


def main():
    print("Scraping StepStone...")
    stepstone_jobs = scrape_stepstone()

    print("Scraping Indeed...")
    indeed_jobs = scrape_indeed()

    # print("Scraping LinkedIn...")
    # linkedin_jobs = scrape_linkedin()

    all_jobs = {
        "StepStone": stepstone_jobs,
        "Indeed": indeed_jobs,
        # "LinkedIn": linkedin_jobs
    }

    send_email(all_jobs)


if __name__ == "__main__":
    main()
