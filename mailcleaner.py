MAIL_SERVER = 'mail.server.com' #mail server hostname or IP
MAX_DAYS = 30 #If your message older than 30 days it will be deleted
import csv
import imaplib
import datetime

accounts = {}
with open('accounts.csv') as f:
    accounts = dict(filter(None, csv.reader(f, delimiter=';'))) 
print(accounts)
today = datetime.date.today()
print(today)
cutoff_date = today - datetime.timedelta(days=MAX_DAYS)
before_date = cutoff_date.strftime('%d-%b-%Y')
search_args = '(BEFORE "%s")' % before_date

def cleanbox(mailbox, username, pasword):
    try:
        print(f'{username} with PASS {pasword}')
        imap = imaplib.IMAP4(MAIL_SERVER)
        imap.login(username, pasword)
        imap.select(mailbox)
        typ, data = imap.search(None, 'ALL', search_args)
        for num in data[0].split():
            imap.store(num, '+FLAGS', '\\Deleted')
        imap.expunge()
        imap.close()
        imap.logout()
        print(f"{mailbox} for {username} Done!")
    except:
        print(f"There is no {mailbox} folder for {username}?")

for user, pas in accounts.items():
    cleanbox(mailbox='Junk', username=user, pasword=pas)

for user, pas in accounts.items():
    cleanbox(mailbox='Spam', username=user, pasword=pas)

for user, pas in accounts.items():
    cleanbox(mailbox='Trash', username=user, pasword=pas)
