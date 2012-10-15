'''
Send an email via python using sendmail.
'''

import os

def send(subject, text, from_addr, to_addr, when=''):
	command = "/usr/sbin/sendmail -t -i"
	body = """From: %s\nTo: %s\nSubject: %s\n%s\n""" % (from_addr, to_addr, subject, text)
	p = os.popen('%s'%command, 'w')
	p.write(body)
	if when: 
		p.write('\n | at %s'%when)
	exit_status = p.close()
	if exit_status:
	    print "Error exit status", exit_status

def sendme(text, subject='sent from my computer', when=''):
	from_addr = "" # your address here
	to_addr = "" # your address here
	send(subject, text, from_addr, to_addr, when)
