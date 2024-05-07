import markdown
from bs4 import BeautifulSoup
from datetime import date

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

"""
Returns relevant rows from the markdown table as a 2D array. 
Relevant rows are: 
    Jobs that are for Fall 2024 
    Jobs that are still hiring 
    Jobs in Canada (Maybe)
    Jobs that are still open for 

@Param md - The repo's README.md file
"""
def extract_table(md): 
    parsedMD = markdown.markdown(md, extensions = ['tables'])
    soup = BeautifulSoup(parsedMD, features = "html.parser")
    data = [] 
    
    for r in soup.find_all("tr"):
        c = r.find_all("td")
        if (c == None or len(c) <6): continue

        # Check if the internship is for fall 2024 
        if("Fall 2024" not in c[3].get_text().split(",")): continue

        # Check if Job is still accepting applications (if there are apply links)
        apply_links = []     
        for linkObj in c[4].find_all("a"): 
            apply_links.append(linkObj.get("href"))
        if(len(apply_links) == 0): continue

        row = [c[0].get_text(), c[1].get_text(), c[2].get_text(), apply_links, c[5].get_text()]
        data.append(row)

    return data


f = open("testingRM.md", "r", encoding = "utf-8")

table = extract_table(f.read())

