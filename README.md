# 🕸️ Web Scraper CLI

A simple and efficient command-line tool to scrape job listings from **remoteok.com** based on a keyword or tag.

> 🎯 This project was built as a portfolio piece to demonstrate web scraping and CLI development skills.  
> While minimal, it is **designed to be easily extended** for real-world freelance or client-based projects.

---

## 🚀 Features

- Search job listings by keyword/tag
- Save results in `JSON` or `CSV` format
- Clear and interactive CLI with `argparse`
- Automatically creates `output/` directory if missing

---

## 📥 Example Usage

```bash
# Save jobs related to 'python' in JSON format
python main.py --tag python --output json

# Save jobs related to 'remote' in CSV format
python main.py --tag remote --output csv
````

---

## 📁 Project Structure

```
web-scraper-cli/
│
├── main.py              # Entry point for CLI
├── scraper.py           # Contains scraping logic
│
├── output/              # Directory to store scraped results
│   ├── jobs_python.json
│   └── jobs_remote.csv
│
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignored files config
├── LICENSE              # Project license (MIT)
└── README.md            # Project documentation (this file)

```

---

## ⚙️ Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Used Libraries:

* `requests`
* `beautifulsoup4`
* `pandas`
* `argparse`

---

## 📌 Notes

* This is a **minimal demo** version built for showcasing skills.
* In real-world use cases, additional features can be added, such as:

  * Scraping from multiple sources
  * Handling pagination
  * Scheduling scrapes (cron jobs)
  * Exporting to databases (SQLite, PostgreSQL)
  * Logging and error tracking
  * Proxy & User-Agent rotation

---

## 🗂 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more details.

---

## 🧑‍💻 Author

**Hadi Dadashzade**
[GitHub](https://github.com/hadidadashzade) • [LinkedIn](https://linkedin.com/in/hadidadashzade)
