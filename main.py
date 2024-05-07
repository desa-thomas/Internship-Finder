import requests, repoScraper, emailSender

url = "https://raw.githubusercontent.com/SimplifyJobs/Summer2024-Internships/dev/README-Off-Season.md"
response = requests.get(url) 

print(response.status_code); 
if(response.status_code==200): 
    readme = response.text
    table = repoScraper.extract_table(readme)
    message = emailSender.createEmail(table=table)
    emailSender.sendEmail(message=message)
    print("email sent")

else: 
    print("error: {error}".format(error = response.status_code))