# import smtplib
#
# gmail_user = 'vaclaims.us@gmail.com'
# gmail_password = '123qwe!@#QWE'
#
# sent_from = gmail_user
# to = ['mklekotko@gmail.com']
# subject = 'Important Message!'
# body = 'Hey there, this is the email body.'
#
# # access gmail's SMTP server with Secure Socket Layer (SSL) encryption.
# # pass above variables to the login function and sendmail function.
# try:
#     server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server_ssl.ehlo()
#     server_ssl.login(gmail_user, gmail_password)
#     server_ssl.sendmail(sent_from, to, body)
#     server_ssl.close()
#
# # print success or error message to the console.
#     print 'Email sent!'
# except:
#     print 'Something went wrong...'