import csv
from jobspy import scrape_jobs


def run_job_scraper():
    jobs = scrape_jobs(
        site_name=[
            "indeed",
            "linkedin",
            "zip_recruiter",
            "google",
            "glassdoor",
        ],  # "glassdoor", "bayt", "naukri", "bdjobs"
        search_term="drone",
        google_search_term="drone jobs near Akron, OH since yesterday",
        location="Akron, OH",
        results_wanted=5,
        hours_old=72,
        country_indeed="USA",
        # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
        # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    )
    print(f"Found {len(jobs)} jobs")
    print(jobs.head())
    jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    return "jobs.csv"
