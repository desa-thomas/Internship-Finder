# Internship-Finder
Scrapes postings from [this repository](https://github.com/SimplifyJobs/Summer2025-Internships/blob/dev/README-Off-Season.md) and emails a list of all open postings to email specified in `config.py`. 
## Usage
1. Set up sender, and receiver email in `config.py`. If using Gmail for sender email you have to generate an app password and use that.
2. Run `main.py`
3. Check the receiver email, and it will contain a list of all open fall positions from the repository
