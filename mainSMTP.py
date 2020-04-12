# This file sends an email through gmail's SMTP server.
# inputs: gmail account credentials, a recipient account, a subject and body.

# import smtplib: a native python library for sending emails.
import smtplib

# define variables to store the gmail account credentials.
gmail_user = 'GMAIL ACCOUNT'
gmail_password = 'GMAIL ACCOUNT PASSWORD'

# define variables to be parameters for the sendmail object.
sent_from = gmail_user
to = ['RECIPIENT GMAIL ACCOUNT']
subject = 'Important Message!'
body = 'Hey there, this is the email body.'

# access gmail's SMTP server with Secure Socket Layer (SSL) encryption.
# pass above variables to the login function and sendmail function.
try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(sent_from, to, body)
    server_ssl.close

# print success or error message to the console.
    print 'Email sent!'
except:
    print 'Something went wrong...'
