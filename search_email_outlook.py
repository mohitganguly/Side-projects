import imaplib
import email 
import base64
from email.parser import HeaderParser
import re
import search_email_outlook
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import parseaddr
import datetime


def func():
	mail = imaplib.IMAP4_SSL('email.vanderbilt.edu',993)
	date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
	with open('password_outlook.txt', 'r') as myfile:
		password =  myfile.read()
	PASSWORD = str(base64.b64decode(password))
	
	
	mail.login('gangulm', PASSWORD)
	#mail.list()
	status, messages = mail.select('INBOX')

	#num=0

	resp, items = mail.search(None, 'UNSEEN')
	
	items = items[0].split()
	
	
	#items = int(items[0])
	#print int(items[0])
	#print len(items)
	s =[]
	for num in items:
		rv, data = mail.fetch(num, '(RFC822)')
		
		msg = email.message_from_string(data[0][1])
#		#print msg['Subject'], msg['Date']
#		#print msg['Subject']
		s = msg["From"]
		
#		if 'duco' in msg['From'] or 'hjc' in msg['From']:
#			i = i + 1	
#		#string = msg.get_payload()[0].get_payload()
#		#if 'exceeds' in msg['Subject']:
#			#print ('foo')
##			a = re.findall(r'\d+\.\d+', string)
##			print float(a[-1])
##			#print msg['Subject']
	
	#return len(items)
	#return i
	#return items, msg['From']
	return len(items), s
	
#print search_email_outlook.func()
