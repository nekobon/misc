'''
downloader.py

Yu Tomita
yu.t@gatech.edu
2008

Download a file from url to a given loaction.
'''

# So far, it only supports downloading a file from url
import urllib
import os.path

def download(url,folder,option=None):
	'''
	available options
	'a' = alternate names if exists already
	's' = skip if exists already
	'''
	if folder[-1] != '/':
		folder += '/'
	filenameto = folder+url.split('/')[-1]
	i = 1
	if option == 's' and os.path.isfile(filenameto):
		print ' ** Skipped ** File already exists at %s'%filenameto
		return
	if option == 'a':
		nonext = filenameto.split('.')[-2]
		ext = filenameto.split('.')[-1]
		while os.path.isfile(filenameto):
			#print '%s \t already exists'%filenameto
			i+=1
			filenameto = nonext + str(i) + '.' + ext
	filefrom = urllib.urlopen(url)		
	fileto = open(filenameto,'w')
	fileto.write(filefrom.read())
	print ' ** Saved ** File Saved to %s'%filenameto	
	filefrom.close()
	fileto.close()

def dl(url,folder,option=None):
	download(url,folder,option)
