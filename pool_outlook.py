import time
import os
import imaplib
import email 
import base64
from email.parser import HeaderParser
import re
#import search_email_outlook
import search_email_outlook
import send_sms
import return_total


while True:
	[v1, name] = search_email_outlook.func()
	print v1, name
	if 'Jansen'  in name:
		print ('mismatch')
		send_sms.func1('Email from Duco')
		print ("text sent")
	if 'Chiel'  in name:
		print ('mismatch')
		send_sms.func1('Email from Chiel')
		print ("text sent")
	if 'Oian'  in name:
		print ('mismatch')
		send_sms.func1('Email from Chad')
		print ("text sent")
	#time.sleep(5)
	
	
