# This is the Main file for the program
import smtplib
import csv

sender_gmail = 'vaclaims.us@gmail.com'
sender_password = '123qwe!@#QWE'
recipient_gmail = ['m.mccall88@gmail.com']
body = 'Email sent successfully.'

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.login(sender_gmail, sender_password)
    server_ssl.sendmail(sender_gmail, recipient_gmail, body)
    server_ssl.close()
    print 'Email sent!'

except:
    print 'Something went wrong...'

# this section is for handling CSV files
# with open('MOCK.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)
