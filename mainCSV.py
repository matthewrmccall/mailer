# # This is the Main file for the program
import smtplib
import csv

sender_gmail = 'vaclaims.us@gmail.com'
sender_password = '123qwe!@#QWE'
body = 'Email sent successfully.'

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

