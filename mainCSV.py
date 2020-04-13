# # This is the Main file for the program
# 04.13.2020 - opens and reads the project CSV and sends an email to the first entry in row 3 of excel ('2' here)
import smtplib
import csv

# vaclaims.us@gmail.com
sender_gmail = 'vaclaims.us@gmail.com'
# 123qwe!@#QWE
sender_password = '123qwe!@#QWE'
body = 'You were referred by a friend. \n To our VA claims prep service.'

# this section is for handling CSV files
with open('MOCK.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if len(row[2]) > 1:
            recipient_gmail = row[2]

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.login(sender_gmail, sender_password)
    server_ssl.sendmail(sender_gmail, recipient_gmail, body)
    server_ssl.close()
    print 'Email sent!'

except:
    print 'Something went wrong...'

