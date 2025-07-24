# main.py

import argparse
from scraper import scrape_jobs

def main():
    parser = argparse.ArgumentParser(description="Remote Job Scraper CLI")
    parser.add_argument(
        "--tag",
        type=str,
        required=True,
        help="Job tag to search for (e.g., python, designer, ai)"
    )
    parser.add_argument(
        "--output",
        type=str,
        choices=["json", "csv"],
        default="json",
        help="Output format: json or csv (default: json)"
    )
    args = parser.parse_args()

    print(f"🔍 Searching jobs for tag: {args.tag}")
    scrape_jobs(tag=args.tag, output_format=args.output)

if __name__ == "__main__":
    main()
