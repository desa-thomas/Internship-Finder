import smtplib, ssl, config
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from datetime import date

"""
Creates email HTML message using table extracted from repoScraper
"""
def createEmail(table):
    message = MIMEMultipart("alternative")
    message["Subject"] = str(date.today().strftime("%b %d")) + " Postings"
    message["From"] = config.sender_email
    message["To"] = config.receiver_email

    text = """\
    Plain text version: 
    """
    html = """\
    <html>
    <body>
        <h2> {heading} </h2> 
        <p>
    """.format(heading = str(len(table)) + " postings")
    for t in table:
        html += "<a href = {link}> {text} </a>".format(link = (t[3])[0], text = t[0] +" "+ t[1])
        html += " " + t[2] + " " + t[4]
        html += "<br>"
    
    html += """\
    </p>
    </body>
    </html>
    """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    
    return message 

def sendEmail(message): 
    port = 465
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: 
        server.login(config.sender_email, config.password)
        server.sendmail(config.sender_email, config.receiver_email, message.as_string())
