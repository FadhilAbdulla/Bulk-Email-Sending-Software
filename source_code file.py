import pandas as pd
import smtplib
from tkinter import*

#username and password
username = "your email"
password = "your password"
#read excel
e = pd.read_excel("data file in xls")
emails = e["email"].values
names = e["name"].values
#set smtp
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
#login in your gmail account
server.login(username,password)
#enter your subject
subject = "enter your subject here"
#abbrevation
abbr = "Hi "
#message of the body
message = '''
this is a sample message by fadhil for testing bulk message sending

Regards,
Fadhil Abdulla'''

#mailing process

for i in range(0,len(emails)):
    name = names[i]
    email = emails[i]
    full_message = abbr + name + message
    body = "subject: {}\n\n{}".format(subject,full_message)
    #server.sendmail(username,email,body)
    print(email+" sent succesfully")


server.quit()
