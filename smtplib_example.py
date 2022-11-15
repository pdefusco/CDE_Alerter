from smtplib import SMTP_SSL

smtp_server = 'smtp.acme.com'
smtp_port = 465
smtp_user = 'svcaccuser@acme.com'
smtp_password = 'svcacctpwd'

sent_from = smtp_user
to = ['pauldefusco@cloudera.com']
subject = 'test message'
body = '''
Hey, what's up?

Andre
'''

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(smtp_user, smtp_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
    raise
